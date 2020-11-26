#This is a very much work in progress.
import platform
import ipaddress
import csv
from address import IpAddress
from operating_system import OperatingSystem

print(" ༼ つ ◕_◕ ༽つ Welcome to Knowsy!  I know everything about IP addresses and Domains(coming soon).")

#Determine Operating System information
#This may be removed as program is being developed as OS agnostic
print(f"\n ༼ つ ◕_◕ ༽つ Let's check what operating system you are running.")

os_check =  platform.system()
current_os = OperatingSystem(os_check)
current_os.set_os()
current_os.return_os()

#NOTE: print statements and hardcoded IPs for testing
#TODO for host in host_list.csv, run checks, add to csv

#Test Vars for CSV
testip = "9.9.9.9"
testdomain = "quad9.com"
testping = 'Yes'
testroute = '10.0.1.1 > 6.7.8.9 > 9.9.9.1'

#Create and Setup the CSV
name_request = input(" ༼ つ ◕_◕ ༽つ Save Knowsy CSV file as? ")
filename = name_request + '.csv'

with open(filename, 'w') as file_object:
    file_writer = csv.writer(file_object, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    file_writer.writerow(['IP', 'Domain', 'Ping', 'Routes'])

#Ask user for whole file
#TODO validate file exists, exception catch
hostfile = input(" ༼ つ ◕_◕ ༽つ What is the name of your host file (.txt ONLY)? ")

print("༼ つ ◕_◕ ༽つ Knowsy has begun the process of putting it's Knowse in things...")

with open(hostfile, "r") as h_file:
    for host in h_file:
        #Validate IP
        ip = IpAddress(host.rstrip())
        if ip.validate_ip():
            #Ping Test
            ping_answer = ip.ping_check(current_os.return_os())
            with open(filename, 'a') as file_object:
                file_writer = csv.writer(file_object, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                file_writer.writerow([ip.return_ip_address(), testdomain, ping_answer, testroute])
        else:
            with open(filename, 'a') as file_object:
                file_writer = csv.writer(file_object, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                file_writer.writerow([ip.return_ip_address(), 'Invalid IP', 'Invalid IP', 'Invalid IP'])

print("༼ つ ◕_◕ ༽つ Knowsy Knows things about your network.  Your CSV is ready!")