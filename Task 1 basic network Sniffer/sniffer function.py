#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 14:03:06 2024

@author: mahsa
"""
def sniffing(host, socket_protocol, timeout=10):
    try:
        # Create a raw socket
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
        
        # Bind the socket to the host
        s.bind((host, 0))

        # Include IP headers in the captured packets
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

        # Set timeout to avoid indefinite blocking
        s.settimeout(timeout)

        # Sniffing loop
        while True:
            # Capture packets
            packet = s.recvfrom(65565)
            
            # Extract packet content and IP header
            packet = packet[0]
            ip_header = packet[0:20]  # Assuming IPv4
            
            # Unpack IP header fields
            iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
            
            # Version and Header Length
            version_ihl = iph[0]
            version = version_ihl >> 4
            ihl = version_ihl & 0xF
            
            # Create a dictionary to store IP header fields
            ip_header_fields = {
                'Version': version,
                'Header Length': ihl * 4,
                'TTL': iph[5],
                'Protocol': iph[6],
                'Source Address': socket.inet_ntoa(iph[8]),
                'Destination Address': socket.inet_ntoa(iph[9])
            }
            
            # Print IP header fields
            print('\n'.join(f'{field}: {value}' for field, value in ip_header_fields.items()))

    except socket.error as e:
        print(f'Error: {e}')

    except KeyboardInterrupt:
        print("\nProcess interrupted.")

