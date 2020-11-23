import ipaddress


class IpAddress:
    """Represents an IP address"""

    def __init__(self, address):
        """Initialize an ip address"""
        self.set_ip_address(address)
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