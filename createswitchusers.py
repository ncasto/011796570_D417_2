from netmiko import ConnectHandler
from getpass import getpass


userswitch = { 
    "device_type": "extreme_exos",
    "host": "10.10.1.22",
    "username": "admin",
    "password": ''
}

acctswitch = { 
    "device_type": "extreme_exos",
    "host": "10.10.1.32",
    "username": "admin",
    "password": ''
}

MGMTswitch = { 
    "device_type": "extreme_exos",
    "host": "10.10.1.31",
    "username": "admin",
    "password": ''
}


ITswitch = { 
    "device_type": "extreme_exos",
    "host": "10.10.1.30",
    "username": "admin",
    "password": ''
}

create_user_cmd = "create account admin Local_admin WGU123"
# Command to show accounts
show_accounts_cmd = "show accounts"

# Function to connect to the switch and create the user account, then show accounts
def create_and_show_user(switch):
    with ConnectHandler(**switch) as net_connect:
        output = net_connect.send_command(create_user_cmd)
        output += net_connect.send_command(show_accounts_cmd)
        output += net_connect.save_config()
    return output

# Create the user on each switch and show accounts
print("Creating user on DMZ switch and showing accounts...")
print(create_and_show_user(userswitch))

print("Creating user on Admin switch and showing accounts...")
print(create_and_show_user(acctswitch))

print("Creating user on User switch and showing accounts...")
print(create_and_show_user(MGMTswitch))

print("Creating user on User switch and showing accounts...")
print(create_and_show_user(ITswitch))
