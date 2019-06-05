#Import some of required modules
import telnetlib
#import ftplib
import time
import os

###PUT APPROPRIATE USER & PASSWORD
username = ''
password = ''

###PREPARE LIST OF DEVICES AS INPUT
with open (r'device_list.txt', 'r') as ip_input:
    for ip in ip_input:
        host = ip.strip()
        ip = ip.strip("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-" + "\n")
        print(ip)

        telnet = telnetlib.Telnet(ip)
        telnet.read_until(b'Password: ', 3)
        telnet.write(password.encode('ascii') + b"\n")
        telnet.write(b"enable\n")
        telnet.read_until(b'Password: ', 3)
        telnet.write(password.encode('ascii') + b"\n")
        telnet.write(b"terminal length 0\n")
        telnet.write(b"show power inline | i Ieee PD             0\n")
        telnet.write(b"exit\n")
        output = telnet.read_all()
        #print(output)


##################
#OUTPUT GENERATED FOR FILES
###########################
        mytime = time.strftime('%Y-%m-%d-%H-%M')
#Remove the trailing /n from varible ip this is required for file creation
#ip = ip.strip(' \t\n\r')

        filename = ("NETVIRTdev-" + mytime)
        filepath = os.path.join('NETVIRT_DEV_LIST', host, filename)

        if not os.path.exists(os.path.dirname(filepath)):
            os.makedirs(os.path.dirname(filepath))
        with open(filepath, "wb") as f:
            f.write(output)
            f.close()
###OPEN FILE / TAKE RQRD INTF / SHUT / NO SHUT
        with open(filepath) as gifile:
            for line in gifile:
                if 'Gi' in line:
                    giintf = line[:8]
                    giintf2 = 'interface ' + giintf
                    #print(giintf2)
                    #print(ip)
                    telnet2 = telnetlib.Telnet(ip) 
                    telnet2.read_until(b'Password: ', 3)
                    telnet2.write(password.encode('ascii') + b"\n")
                    telnet2.write(b"enable\n")
                    telnet2.read_until(b'Password: ', 3)
                    telnet2.write(password.encode('ascii') + b"\n")
                    #telnet2.write(b"terminal length 0\n")
                    telnet2.write(b"config term\n")
                    #print(giintf2.encode('ascii'))
                    telnet2.write(giintf2.encode('ascii') + b"\n")
                    telnet2.write(b"shutdown\n")
                    time.sleep(2)
                    telnet2.write(b"no shutdown\n")
                    telnet2.write(b"end\n")
                    time.sleep(2)
                    telnet2.write(b"exit\n")
                    time.sleep(3)


###NEPOTREBAN U SLUCAJU WHILE PETLJE gifile.close()
