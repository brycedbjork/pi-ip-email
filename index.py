import requests
import socket
import fcntl
import struct


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


ip = get_ip()

r = requests.post("https://api.mailgun.net/v3/mg.sandboxatyale.com/messages", auth=("api", "255f445b4e76bfadfba7bf961a98592d-4a62b8e8-9a66ec05"), data={"from": "Bryce's Pi <bryces-pi@sandboxatyale.com>",
                                                                                                                                                        "to": ["bryce.bjork@yale.edu"],
                                                                                                                                                        "subject": "Pi IP",
                                                                                                                                                        "text": ip})
