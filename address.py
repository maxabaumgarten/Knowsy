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
                return print(f"{self.address} cannot be pinged from this host.")
            elif ("Lost = 3" or "Lost = 2") in self.ping_result:
                return print(f"The connection to {self.address} is shaky from this host.")
            else:
                return print(f"{self.address} can be pinged from this host.")
        #Linux Ping Check
        elif operating_sys == 'linux':
            self.ping_result = str(subprocess.run(['ping', '-c4', '-w4', self.address], stdout=subprocess.PIPE))
            if "100% packet loss" in self.ping_result:
                return print(f"{self.address} cannot be pinged from this host.")
            elif "0% packet loss" in self.ping_result:
                return print(f"{self.address} can be pinged from this host.")
            else:
                return print(f"The connection to {self.address} is shaky from this host.")
        #Apple Ping Check
        elif operating_sys == 'apple':
            return print(f"Management hasn't paid for a $1,000 laptop shaped iPad yet.")