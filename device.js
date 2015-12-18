import HTML
import socket
import psutil
import commands

net_connections = psutil.net_connections(kind='inet')
netcon = psutil.net_io_counters(pernic=True)
CPU = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()

def get_cpu_temp_celsius():
    tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
    cpu_temp = tempFile.read()
    tempFile.close()
    return float(cpu_temp)/1000

HOST, PORT = '', 8881
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'serving HTTP on port %s ...' % PORT
while True:
	client_connection, client_address = listen_socket.accept()
	request = client_connection.recv(1024)
	print request


	http_status = "HTTP/1.1 200 OK \n"

	http_type = "Content-type: text/html\n"
	
	
	connections = ""
	for conn in psutil.net_connections(kind='inet'):
		connections = connections + str(conn.raddr) +"</br>"

	table_connections = HTML.Table(header_row=['Name', 'reading'])

	for conn in psutil.net_connections(kind='inet'):
		table_connections.rows.append(['connected', str(conn.raddr)])


	table_data = [

	['CPU PERCENTAGE',str(CPU)],
	['Memory' ,str(memory)],
	['cpu temp',str(get_cpu_temp_celsius())],
	['packets_sent',str(netcon['wlan0'].packets_sent)],
	['packets_recv',str(netcon['wlan0'].packets_recv)],
	['packets_dropped',str(netcon['wlan0'].dropin)],
	['error packets',str(netcon['wlan0'].errin)],
	
	]

	


	HTML_COLORS = ['Black', 'Green']

	cputable = HTML.Table(table_data,header_row=['Name', 'reading'])
	
	Temp_readings = [20,21,22,25,28,12,31,76,67,40,12,21,23,34,1,22,23,26]
	
	
	

	for temp in sorted(Temp_readings):
		if temp > 70:
			color = 'Red'
			result = 'Extreme' 
		elif temp > 40:
			color = 'Yellow'
			result = 'Warning'
			
		else:
			color = 'Green'
			result = 'ok'




	http_body = """
		<!doctype html>
		<html>
		<head>
		<meta http-equiv="refresh"
		content="10">
		<body>
		<h2> System Information </h2>
		""" + str(cputable) + """
		</br> <p> 
		</p>
		<h2> Remote Connections </h2>
		<p>
		""" + str(table_connections) + """ </p>
		<p>
		""" + str(Temptable) + """ </p>
		</body>
		</html>"""



	


	client_connection.send(http_status)
	client_connection.send(http_type)

	client_connection.send(http_body)
	client_connection.close()