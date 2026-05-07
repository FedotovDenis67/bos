#!/usr/bin/env python3
from scapy.all import sniff, ARP
import syslog
import time

ip_mac_map = {}

def log_alert(msg):
    with open("/var/log/arp_detection.log", "a") as f:
        f.write(f"[{time.ctime()}] ALERT: {msg}\n")
    syslog.syslog(syslog.LOG_WARNING, f"ARP Spoofing: {msg}")
    print(f"[!] {msg}")

def detect_spoof(pkt):
    if pkt[ARP].op == 2:
        ip = pkt[ARP].psrc
        mac = pkt[ARP].hwsrc
        if ip in ip_mac_map and ip_mac_map[ip] != mac:
            log_alert(f"IP {ip} changed MAC from {ip_mac_map[ip]} to {mac}")
        else:
            ip_mac_map[ip] = mac

print("[*] ARP spoofing detector started. Press Ctrl+C to stop.")
sniff(filter="arp", prn=detect_spoof, store=0)
