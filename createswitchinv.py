import configparser

config = configparser.ConfigParser()

config['User_NetworkSwitch'] = {
    'RAM': '512 MB',
    'vCPUs': '1',
    'Qemu Binary': '/bin/qemu-system-x86_64 (v4.2.1)',
    'Boot Priority': 'CD/DVD-ROM or HDD',
    'On Close': 'Power off the VM' ,
    'Console type': 'telnet',
    'Adapters': '13',
    'Base MAC': '0c:e0:f2:0b:00:00',
    'Type': 'Realtek 8139 Ethernet (rtl8139)',
    'Replicate network connection states in Qemu': 'Yes'
}

config['ACCT_NetworkSwitch'] = {
    'RAM': '512 MB',
    'vCPUs': '1',
    'Qemu Binary': '/bin/qemu-system-x86_64 (v4.2.1)',
    'Boot Priority': 'CD/DVD-ROM or HDD',
    'On Close': 'Power off the VM',
    'Console type': 'telnet',
    'Adapters': '13',
    'Base MAC': '0c:40:34:07:00:00',
    'Type': 'Realtek 8139 Ethernet (rtl8139)',
    'Replicate network connection states in Qemu': 'Yes'
}

config['MGMT_NetworkSwitch'] = {
    'RAM': '512 MB',
    'vCPUs': '1',
    'Qemu Binary': '/bin/qemu-system-x86_64 (v4.2.1)',
    'Boot Priority': 'CD/DVD-ROM or HDD',
    'On Close': 'Power off the VM',
    'Console type': 'telnet',
    'Adapters': '13',
    'Base MAC': '0c:6f:af:13:00:00',
    'Type': 'Realtek 8139 Ethernet (rtl8139)',
    'Replicate network connection states in Qemu': 'Yes'
}

config['IT_NetworkSwitch'] = {
    'RAM': '512 MB',
    'vCPUs': '1',
    'Qemu Binary': '/bin/qemu-system-x86_64 (v4.2.1)',
    'Boot Priority': 'CD/DVD-ROM or HDD',
    'On Close': 'Power off the VM',
    'Console type': 'telnet',
    'Adapters': '13',
    'Base MAC': '0c:1c:b2:85:00:00',
    'Type': 'Realtek 8139 Ethernet (rtl8139)',
    'Replicate network connection states in Qemu': 'Yes'
}

with open('switchinventory.ini', 'w') as configfile:
    config.write(configfile)
