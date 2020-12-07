#TODO #1 class for ingesting .TXT and .CSV files and output .CSV files
import csv

class TheCSV:
    """Represents a CSV File"""
    
    def __init__(self, csv_file):
        """Initializes a CSV object"""
        self.csv_file =  csv_file
        self.create_csv()

    def create_csv(self):
        """Creates the CSV File"""
        with open(self.csv_file, 'w') as file_object:
            file_writer = csv.writer(file_object, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow(['IP', 'Domain', 'Related_IPs', 'Ping', 'Routes'])
    
    def append_csv(self, ip, domain, related_ips, ping, routes):
        """Add data to the CSV"""
        with open(self.csv_file, 'a') as file_object:
            file_writer = csv.writer(file_object, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow([ip, domain, related_ips, ping, routes])