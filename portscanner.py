import socket
import sys
import datetime

# 

remoteServer = "localhost"

remoteServerIP = socket.gethostbyname(remoteServer)

# 
print "_" * 60

print "please wait, scanning remote host", remoteServerIP

print "_" * 60

for port in range (1, 1025):

	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			print "port {}: \t open".format(port)

		sock.close()

	except socket.gaierror:

			print 'hostname could not be resolved. Exiting'

			sys.exit()

	except socket.error:

			print "couldn't connect to server"

			sys.exit()
	