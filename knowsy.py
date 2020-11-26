#This is a very much work in progress.
import platform
import ipaddress
from address import IpAddress
from operating_system import OperatingSystem

print("Welcome to Knowsy!  I know everything about IP addresses and Domains(coming soon).")

#Determine Operating System information
#This may be removed as program is being developed as OS agnostic
print(f"\nLet's check what operating system you are running.")

os_check =  platform.system()
current_os = OperatingSystem(os_check)
current_os.set_os()
current_os.return_os()

#NOTE: print statements and hardcoded IPs for testing
#TODO for host in host_list.csv, run checks, add to csv

#ip_input = input("What IP address do you want to know about? ")

#Offline IP
ip = IpAddress("10.10.10.10")
if ip.validate_ip():
    ip.ping_check(current_os.return_os())
else:
    print(f"{ip.return_ip_address()} is not valid.")

#Valid IP
ip.set_ip_address("1.1.1.1")
if ip.validate_ip():
    ip.ping_check(current_os.return_os())
else:
    print(f"{ip.return_ip_address()} is not valid.")

#Invalid IP
ip.set_ip_address("codingiscool")
if ip.validate_ip():
    ip.ping_check(current_os.return_os())
else:
    print(f"{ip.return_ip_address()} is not valid.")