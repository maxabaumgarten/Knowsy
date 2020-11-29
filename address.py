import ipaddress
import os
import subprocess
import socket

class IpAddress:
    """Represents an IP address"""

    def __init__(self, address):
        """Initialize an ip address"""
        self.address = address
        self.validate_ip()

    def validate_ip(self):
        """Check's if the IP is valid."""
        try:
            ipaddress.ip_address(self.address)
            return True
            # return print(f"'{self.address}' is a valid IP address.")
        except ValueError:
            return False
            # return print(f"'{self.address}' is not a valid IP address.")

    def return_ip_address(self):
        return self.address

    def set_ip_address(self, input_ip):
        self.address = input_ip
        self.validate_ip()

    def ping_check(self, operating_sys):
        """Performs a ping check against the IP with 4 pings."""
        #Windows Ping Check
        if operating_sys == 'windows':
            self.ping_result = str(subprocess.run(['ping', self.address], stdout=subprocess.PIPE))
            if "Lost = 4" in self.ping_result:
                return "No"
            elif ("Lost = 3" or "Lost = 2") in self.ping_result:
                return "Shaky"
            else:
                return "Yes"
        #Linux Ping Check
        elif operating_sys == 'linux':
            self.ping_result = str(subprocess.run(['ping', '-c4', '-w4', self.address], stdout=subprocess.PIPE))
            if "100% packet loss" in self.ping_result:
                return "No"
            elif "0% packet loss" in self.ping_result:
                return "Yes"
            else:
                return "Shaky"
        #Other Ping Check
        else:
            return print(f"Put a feature request in @ https://github.com/maxabaumgarten/Knowsy.")
    
    def dns_check(self):
        """Performs a DNS lookup on the provided IP"""
        try:
            return socket.gethostbyaddr(self.address)
        except:
            return "No DNS Entry"

    def trace_check(self, operating_sys):
        """Performs a traceroute to the IP with max 30 Hops"""
        if operating_sys == 'windows':
            self.trace_result = str(subprocess.run(['tracert', '/h', '30', self.address], stdout=subprocess.PIPE))
            return self.trace_result
        elif operating_sys == 'linux':
            self.trace_result = str(subprocess.run(['traceroute', self.address], stdout=subprocess.PIPE))
            return self.trace_result
        else:
            return "WERE WORKIN ON IT! Feature request  @ https://github.com/maxabaumgarten/Knowsy."