from netmiko import ConnectHandler
from winrm.protocol import Protocol
import crypt 

inventory = {
    'windowsdesktop1': {'host': '10.10.1.35'},
    'windowsdesktop2': {'host': '10.10.1.36'},
    'windowsdesktop3': {'host': '10.10.1.43'},
    'windowsserver4': {'host': '10.10.1.29'},
    'linuxtest_box1': {'host': '10.10.1.56'},
    'linuxtest_box2' : {'host' : '10.10.1.57'}

}

ssh_username = 'student'
ssh_password = 'P@ssw0rd'
winrm_username = 'student'
winrm_password = 'P@ssw0rd'
sudo_password = 'P@ssw0rd'

def create_user(hostname, username, password_str):
    if 'test' in hostname:
        device_type = 'linux'
        hashed_password = crypt.crypt(password_str, crypt.mksalt(crypt.METHOD_SHA512))
        command = f"sudo useradd -m -p '{hashed_password}' {username}"
        device = {
            'device_type': 'linux',
            'host': inventory[hostname]['host'],
            'username': ssh_username,
            'password': ssh_password,
            'global_delay_factor': 2,
            'verbose' : True
        }
        try:
            with ConnectHandler(**device) as conn:
                output = conn.send_command_timing(command)
                if 'password' in output.lower():
                  output += conn.send_command_timing(sudo_password)
        except Exception as e:
            print(f"Error creating user on {hostname}: {e}")
    elif 'windows' in hostname:
        device_type = 'windows'
        command = f"net user {username} {password_str} /add"
        winrm_session = Protocol(
            endpoint=f"http://{inventory[hostname]['host']}:5985/wsman",
            transport='ntlm',
            username=winrm_username,
            password=winrm_password,
            server_cert_validation='ignore'
        )
        try:
            shell_id = winrm_session.open_shell()
            command_id = winrm_session.run_command(shell_id, command)
            stdout, stderr, return_code = winrm_session.get_command_output(shell_id, command_id)
            winrm_session.cleanup_command(shell_id, command_id)
            winrm_session.close_shell(shell_id)
            print(f"User '{username}' created successfully on {hostname}.")
        except Exception as e:
            print(f"Error creating user on {hostname}: {e}")
    else:
        print(f"Unsupported device type for {hostname}")


for host, details in inventory.items():
    print(f"Creating user on {host}")
    if 'linux' in host:
        username = f"linuxuser{host[-1]}"
    elif 'windows' in host:
        username = f"windowsuser{host[-1]}"
    else:
        print(f"Unsupported device type for {host}")
        continue
    create_user(host, username, 'WGU123')
    
print("login created on test_box1")
print("login created on test_box2")
