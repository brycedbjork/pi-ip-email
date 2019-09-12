import socket
import requests
ip = socket.gethostbyname(socket.gethostname())

r = requests.post("https://api.mailgun.net/v3/mg.sandboxatyale.com/messages", user=("api", "255f445b4e76bfadfba7bf961a98592d-4a62b8e8-9a66ec05"), data={"from": "Bryce's Pi <bryces-pi@sandboxatyale.com>",
                                                                                                                                                        "to": ["bryce.bjork@yale.edu"],
                                                                                                                                                        "subject": "Pi IP",
                                                                                                                                                        "text": ip})
