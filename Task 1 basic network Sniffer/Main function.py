#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 14:03:38 2024

@author: mahsa
"""

def main():
    host = socket.gethostbyname(socket.gethostname())
    print(f'Starting Network Sniffer on {host}')

    # Protocol to sniff (IPPROTO_IP - IP Protocol)
    socket_protocol = socket.IPPROTO_IP

    # Start sniffing
    sniffing(host, socket_protocol)

if __name__ == '__main__':
    main()
