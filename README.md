# Knowsy
A python program that tells you everything you want to know about an IP address or Domain Name.

# Planned Functionality
- Knowsy will accept .txt or .csv files with a list of IP addresses and/or domains.
- Knowsy will perform a Ping Check, DNS Lookup, Traceroute, and potentially an OS Identifier (via NMAP) on each entry
- Knowsy will then format a CSV file with all the information it found about the IPs or Domains.

# Forseable Issues
- Pinging against non-existent/non-pingable IPs or Domains may cause significant slow downs
- Traceroute to non-existent/non-pingable IPs or Domains may cause significant slow downs

# Status
This is as pre-alpha as it gets.
