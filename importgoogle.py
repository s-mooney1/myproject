import socket

ipaddress = str(raw_input("enter ip address"))

hostname= socket.getfqdn (ipaddress)

print hostname