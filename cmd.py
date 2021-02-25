#Python script for running commands to cisco IOS 

import netmiko

connection = netmiko.ConnectHandler(ip="172.16.0.1", device_type="cisco_ios", username="jbarnard", password="Wantage1972")

print(connection.send_command("sh ip int br"))
connection.disconnect()

