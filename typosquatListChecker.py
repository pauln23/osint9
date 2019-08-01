import whois
import socket
from abuseipdb import *
import requests

IPDB = AbuseIPDB("daf6c70bb7c4180f2189077002f7ec8f26f5fd45a539b1d2f37cb567b74139973d696d631a7e899e")


def checkRegistered(domain):
    socket.setdefaulttimeout(2)
    registered = False

    try:
         whois.whois(domain)
         IP = socket.gethostbyname(domain)
         registered = True
         data = (IPDB.check(IP))
         return domain, IP, registered, data.abuseConfidenceScore, data.countryName

    except Exception:
        registered = False
        return domain, 'n/a', registered, 'n/a', 'n/a'


def checkIP(IP):
    hasHosts = False
    data = (IPDB.check(IP))
    hostname = []
    try:
        hostname = socket.gethostbyaddr(IP)
        hasHosts = True
        return IP, hasHosts, hostname, data.abuseConfidenceScore, data.countryName

    except Exception:
        hasHosts = False
        return IP, hasHosts, 'n/a', data.abuseConfidenceScore, data.countryName


