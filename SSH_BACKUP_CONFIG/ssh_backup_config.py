#
#This is an example of a script developed to connect and backup cisco device configs using python
#
import paramiko
import ftplib
import time
import os

def disable_paging(remote_conn):
    '''Disable paging on a Cisco router'''

    remote_conn.send("terminal length 0\n")
    time.sleep(1)

# Clear the buffer on the screen
    output = remote_conn.recv(1000)

    return output

if __name__ == '__main__':

# VARIABLES THAT NEED CHANGED
#ip = '10.18.113.16'
#ipaddress = open('list.txt')
    username = 'dragan.ilic'
    password = 'wersdf123!'
    port = '22'

with open (r'list.txt', 'r') as ip_input:
    for ip in ip_input:
        ip = ip.strip()

# Create instance of SSHClient object
        remote_conn_pre = paramiko.SSHClient()

# Automatically add untrusted hosts (make sure okay for security policy in your environment)
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# initiate SSH connection
        remote_conn_pre.connect(ip, port=port, username=username, password=password)
        print '#################################################'
        print "SSH connection established to %s" % ip

# Use invoke_shell to establish an 'interactive session'
        remote_conn = remote_conn_pre.invoke_shell()
# print "Interactive SSH session established"

# Strip the initial router prompt
        output = remote_conn.recv(1000)

# See what we have
#print output

# Turn off paging
disable_paging(remote_conn)

# Now let's try to send the router a command
# remote_conn.send("\n")
# remote_conn.send("show ip int brief\n")

# These are only required if you need an enable password to login
# remote_conn.send("en\n")
# remote_conn.send("cisco\n")

remote_conn.send("\n")
output = remote_conn.recv(0)
#output = ''
remote_conn.send("show run\n")

remote_conn.send("copy running-config ftp://netvirtexpert.zapto.org/cme-backup\n")

# Wait for the command to complete
time.sleep(2)

output = remote_conn.recv(500000000)

# print output
# print output

##################
#OUTPUT GENERATED FOR FILES
###########################
mytime = time.strftime('%Y-%m-%d-%H-%M-%S')
#Remove the trailing /n from varible ip this is required for file creation
ip = ip.strip(' \t\n\r')
print
print ip + ' config backup in place'
print
#filename = 'tas_%s.txt' % str(ip)
#filename = os.path.join('GigaKOM-', mytime)
filename = ("GigaKOM-" + mytime)
filepath = os.path.join('configs', ip, filename)

if not os.path.exists(os.path.dirname(filepath)):
    os.makedirs(os.path.dirname(filepath))
with open(filepath, "w") as f:
    f.write(output)
    f.close()

###FTP UPLOAD MORA SE SREDI###
#session = ftplib.FTP('netvirtexpert.zapto.org','ra_ftp_user','csc0raftpneD1r@j0v0!')
#os.chdir(os.path.dirname(filepath))
#ftpfile = open("GigaKOM-2018-12-28-11-39-54", 'r')
#session.storbinary('STOR ' + "ftpfile", file)
#ftpfile.close()
#session.quit()

#disconnect
remote_conn.send("exit\n")
print "SSH connection closed to %s" % ip
print '#################################################'
