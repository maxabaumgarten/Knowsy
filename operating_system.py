import os
import platform

class OperatingSystem:
    """A class representing an operating system"""

    def __init__(self, name):
        """Initialize an operating system"""
        self.name = name
    
    def set_os(self):
        """Formats the OS name"""
        formatted_os = self.name.title()
        return print(f"You are running the {formatted_os} operating system.")

    #validate supported operating systems

class Windows(OperatingSystem):
    """Represents a windows operating system"""
    

