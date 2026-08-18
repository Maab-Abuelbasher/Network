# This program will connect to a network device and retrieve the interface status using Netmiko. It will then display the interface status in a readable format.

#import netmiko and os
from netmiko import ConnectHandler  
import os

show_commands = [
    "show ip interface brief",
    #"show version",
    #"show running-config"
]

# Connect to switch using SSH
connection = ConnectHandler(
    host=os.environ.get("router-ip"), username="admin", password=os.environ.get("router-password"), device_type="cisco_ios")

output = ""
for cmd in show_commands:
    output += connection.send_command(cmd) + "\n\n"

print(output)

connection.disconnect()