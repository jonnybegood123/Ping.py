import socket
import sys
import time

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("", 1337))
server.settimeout(10)

while True:
	message = ""
	try:
		message, address = server.recvfrom(1337)
		if message == "done":
			sys.exit()
		if message != "":
			print("Server: Received message " + str(message) + " and sending back to client.")
			server.sendto(str(message), address)
	except socket.timeout:
		print "Server timed out due to not receiving any messages."
		sys.exit()
