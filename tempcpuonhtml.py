import socket
import datetime
import os
import commands

def get_cpu_temp_celsius():
    	tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
    	cpu_temp = tempFile.read()
    	tempFile.close()
    	return float(cpu_temp)/1000

HOST, PORT = '', 8888
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

print 'Serving HTTP on PORT %s ...' % PORT

while True:
	client_connection, client_address = listen_socket.accept()
	request = client_connection.recv(1024)
	print request

	http_response = """\
HTTP/1.1 200 OK

<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<title>Hello World!></title>
	</head>
		<body>

<b>Hello, World!</b>
	<div id="holder" style="width:600px; height:300px">
<p>
The CPU Temperature is
""" + str(get_cpu_temp_celsius())+"""</p>
<p>
The load Average is
""" + str(os.getloadavg()) +"""</p>
</div>
	</body>


</html>

"""

	client_connection.sendall(http_response)
	client_connection.close()


