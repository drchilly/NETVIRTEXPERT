###Device IP to DNAC ID
def ip_to_id(ip):
    return get_url("network-device/ip-address/%s" % ip)['response']['id']

###Get modules from ID
def get_modules(id):
   return get_url("network-device/module?deviceId=%s" % id)


###List ALL modules in device ID
def print_info(modules):
    print("{0:30}{1:15}{2:25}{3:5}".format("Module Name","Serial Number","Part Number","Is Field Replaceable?"))
    for module in modules['response']:
        print("{moduleName:30}{serialNumber:15}{partNumber:25}{moduleType:5}".format(moduleName=module['name'],
                                                           serialNumber=module['serialNumber'],
                                                           partNumber=module['partNumber'],
                                                           moduleType=module['isFieldReplaceable']))
