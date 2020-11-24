#This is a very much work in progress.
import sys
import os
import platform
import ipaddress
import csv
from address import IpAddress
from operating_system import OperatingSystem

print("Welcome to Knowsy!  I know everything about IP addresses and Domains(coming soon).")

#Determine Operating System information
#This may be removed as program is being developed as OS agnostic
print(f"\nLet's check what operating system you are running.")

os_check =  platform.system()
current_os = OperatingSystem(os_check)
current_os.set_os()

ip_input = input("What IP address do you want to know about? ")

ip = IpAddress(ip_input)
print(ip.return_ip_address())
ip.ping_check()

ip.set_ip_address("2.2.2.2")
print(ip.return_ip_address())

ip.set_ip_address("codingiscool")
print(ip.return_ip_address())


#old code
""" while True:
    try:
        ipaddress.ip_address(address)
    except ValueError:
        print(f"'{address}' is not a valid IP address")
        break
    else:
        #determine current operating system
        current_os =  platform.system()
        current_os = current_os.lower()
        print(current_os)

        #each os should be its own class
        #if statement for classes based on OS
        if current_os == 'windows':
            dns_result = os.system('nslookup ' + address)
            ping_result = os.system('ping ' + address)
            trace_result = os.system('tracert ' + address)


            print(dns_result)



        elif current_os == 'linux':
            dns_result = os.system('host ' + address)
            print(dns_result)
        break """

