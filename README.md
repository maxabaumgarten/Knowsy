# ༼ つ ◕_◕ ༽つ Knowsy ༼ つ ◕_◕ ༽つ
A python program that tells you everything you want to know about an IP address or Domain Name.

# What Does Knowsy Do?
- Knowsy accepts a .txt or file with a list of IP addresses (Single Host - /32 Support Only)
- Knowsy will perform a Ping Check, DNS Lookup, Traceroute on each IP given.
- Knowsy will  format a CSV file with all the information it found about the IPs.

# Why use this?
- Knowsy is useful for auditing of network assets.
- Knowsy can help discover network paths/devices.
- Knowsy can be used to perform DNS audits with ease.

# Upcoming Features
- Subnet Support
- DNS Input
- Option Condition Based Domain Lookups (DNS Lookup Only If Ping)
- NMAP OS Detection
- CSV Inputs
- Formated Trace Outputs
- Input/Output File Path Support

# Forseable Issues
- Pinging against non-existent/non-pingable IPs or Domains may cause significant slow downs.
- Traceroute to non-existent/non-pingable IPs or Domains may cause significant slow downs. (Trace Route is now optional.

# Requirements/Dependencies
- Python3
- Traceroute
- NMAP

# How To Use
- Run knowsy.py in same location as <hosts>.txt file.
- Linux users requires 'root' due to subprocess module.

# Status
This is as pre-alpha as it gets.
