import ipaddress
from pythonping import ping

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
    
    def ping_check(self):
        """Performs a ping check against the IP"""
        ping_result = ping(self.address, count=4, verbose=True)
        if "Request timed out" in ping_result:
            return print("That address cannot be pinged from this host.")
        else:
            return ping_result
    
