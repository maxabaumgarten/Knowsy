import ipaddress
import os
import subprocess
import socket

class DomainName:
    """Represents a domain name"""

    def __init__(self, domain):
        """Initialize a domain name"""
        self.domain = domain
    
    
    def name_lookup(self):
        try:
            name_response = socket.gethostbyname_ex(self.domain)[3]
            return name_response
        except:
            return "No DNS Entry"