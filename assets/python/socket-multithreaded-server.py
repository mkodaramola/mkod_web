import socket
from _thread import *


# Set Socket
serversocket = socket.socket()

host = '127.0.0.1'
port = 1233
ThreadCount = 0

# Start Server @127.0.0.1
try:	
	serversocket.bind((host,port))
except socket.error as e:
	print(str(e))

# Start Listening
print("Waiting for connection")
serversocket.listen(5)


def client_thread(connection):
	connection.send(str.encode("Welcome to server"))

	#TransReceive
	while True:
		data = connection.recv(2048)
		addr = str(connection)[str(connection).rindex(',')+2:-2]
		print(""+str(addr)+" sent: "+ str(data.decode("utf-8")))
		if not data:
			break;
		#connection.sendall(str.encode(reply))

	connection.close()


while True:
	
	# Accept Clients
	client, address = serversocket.accept()
	print("Connected to "+str(address[0])+str(address[1]))

	#Thread Multiple Client
	try:
		start_new_thread(client_thread, (client,))
		ThreadCount +=1
		print("ThreadNumber: "+ str(ThreadCount))
	except:
		print("Disconnection Occured")

serversocket.close()














