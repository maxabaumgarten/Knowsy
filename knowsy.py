#This is a very much work in progress.
import platform
import ipaddress
import csv
from address import IpAddress
from operating_system import OperatingSystem

#Knowsy terminal messages
msg_mascot = "༼ つ ◕_◕ ༽つ"
msg_welcome = msg_mascot + " Welcome to Knowsy!  Knowsy knows everything about IP addresses and Domains(coming soon)."
msg_os_check = msg_mascot + " Let's check what operating system you are running."
msg_begin = msg_mascot + " Knowsy has begun the process of putting it's Knowse in things..."
msg_end = msg_mascot + " Knowsy Knows things about your network.  Your CSV is ready!"
msg_csv = msg_mascot + " Save Knowsy CSV file as? "
msg_host = msg_mascot + " What is the name of your host file (.txt ONLY)? "
msg_trace = msg_mascot + " Do you want to traceroute (BETA - Skipping is Faster)? y/n: "

#Default Check Results
#TODO NEED to call defaults instead of last run variable value
ping_answer = "N/A"
dns_answer = "N/A"
trace_answer = "N/A"

#BEGIN
print(msg_welcome)
#Determine Operating System information
print(msg_os_check)

os_check =  platform.system()
current_os = OperatingSystem(os_check)
current_os.set_os()
current_os.return_os()

#TODO for host in host_list.csv, run checks, add to csv

#Create and Setup the CSV
name_request = input(msg_csv)
filename = name_request + '.csv'

with open(filename, 'w') as file_object:
    file_writer = csv.writer(file_object, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    file_writer.writerow(['IP', 'Domain', 'Ping', 'Routes'])

#Ask user for whole file
#TODO validate file exists, exception catch
hostfile = input(msg_host)

#Ask if user wants to trace route
trace_req = None
while trace_req not in ("y", "n"):
    trace_req = input(msg_trace)
    if trace_req == "y":
        continue
    elif trace_req == "n":
        continue
    else:
        trace_req = input(msg_trace)


print(msg_begin)

with open(hostfile, "r") as h_file:
    for host in h_file:
        #Validate IP
        ip = IpAddress(host.rstrip())
        ip_adr = ip.return_ip_address()
        if ip.validate_ip():
            print(f"{msg_mascot} Knowsy is currently pinging {ip_adr}.")
            #Ping Check
            ping_answer = ip.ping_check(current_os.return_os())
            #DNS Check
            print(f"{msg_mascot} Knowsy is finding {ip_adr}'s Domain Name.")
            dns_answer = ip.dns_check()
            #Traceroute Check

            if trace_req == "y":
                print(f"{msg_mascot} Knowsy is tracing the routes to {ip_adr}. (This might take a while...)")
                trace_answer = ip.trace_check(current_os.return_os())
            else:
                print(f"{msg_mascot} is not tracing routes to {ip_adr}.")
            #Write tests to CSV
            with open(filename, 'a') as file_object:
                file_writer = csv.writer(file_object, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                file_writer.writerow([ip_adr, dns_answer, ping_answer, trace_answer])
        else:
            print(f"{msg_mascot} {ip_adr} is not a valid IP address.")
            with open(filename, 'a') as file_object:
                file_writer = csv.writer(file_object, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                #TODO NEED to call defaults instead of last run variable value
                file_writer.writerow([ip_adr + ' (INVALID)', 'N/A', 'N/A', 'N/A'])

print(msg_end)