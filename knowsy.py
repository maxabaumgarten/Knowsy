#This is a very much work in progress.

import sys
import os
import platform
import ipaddress
import csv

#Ask user for IP address
#format/validate input
print("Welcome to Knowsy!  I know everything about IP addresses and Domains(coming soon).")

address = input("What IP address do you want to know about? " )

while True:
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
            dns_result == os.system('dig ' + address)
            print(dns_result)
        break

