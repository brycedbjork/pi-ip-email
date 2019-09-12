import requests
import socket
import fcntl
import struct


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


ip = get_ip_address('eth0')

r = requests.post("https://api.mailgun.net/v3/mg.sandboxatyale.com/messages", auth=("api", "255f445b4e76bfadfba7bf961a98592d-4a62b8e8-9a66ec05"), data={"from": "Bryce's Pi <bryces-pi@sandboxatyale.com>",
                                                                                                                                                        "to": ["bryce.bjork@yale.edu"],
                                                                                                                                                        "subject": "Pi IP",
                                                                                                                                                        "text": ip})
