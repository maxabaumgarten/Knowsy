import ipaddress
import os
import subprocess

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
            return print(f"'{self.address}' is a valid IP address.")
        except ValueError:
            return print(f"'{self.address}' is not a valid IP address.")

    def return_ip_address(self):
        return self.address

    def set_ip_address(self, input_ip):
        self.address = input_ip
        self.validate_ip()
#convert to subprocess from os.system
    def ping_check(self, operating_sys):
        """Performs a ping check against the IP with 4 pings."""
        if operating_sys == 'windows':
            ping_result = subprocess.run('ping ' + self.address, capture_output=True)
            #ping_result = os.system('ping ' + self.address)
            return ping_result
        elif operating_sys == 'linux':
            ping_result = os.system('ping -c4 -w4  ' + self.address)
            return ping_result