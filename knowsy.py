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

ip = IpAddress("10.10.10.10")
if ip.validate_ip():
    ip.ping_check(current_os.return_os())
else:
    print("That address is not valid.")

#print(ip.return_ip_address())
#TODO #2 needs to be conditioned on being a valid IP
#ip.ping_check(current_os.return_os())

ip.set_ip_address("1.1.1.1")
print(ip.return_ip_address())
ip.ping_check(current_os.return_os())

ip.set_ip_address("codingiscool")
print(ip.return_ip_address())