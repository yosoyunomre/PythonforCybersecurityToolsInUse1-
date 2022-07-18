#!/usr/bin/python3
#nmap for port scanning
import nmap
nm = nmap.PortScanner()
scan_range = nm.scan(hosts="127.0.0.1","21-443")
print (scan_range['scan'])

