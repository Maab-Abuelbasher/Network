# This program will connect to a network device and retrieve the interface status using Netmiko. It will then display the interface status in a readable format.

#import netmiko
from netmiko import ConnectHandler  

show_commands = [
    "show ip interface brief",
    #"show version",
    #"show running-config"
]

# Connect to switch using SSH
connection = ConnectHandler(
    host="192.168.8.20", username="admin", password="123456", device_type="cisco_ios")

output = ""
for cmd in show_commands:
    output += connection.send_command(cmd) + "\n\n"

print(output)

connection.disconnect()