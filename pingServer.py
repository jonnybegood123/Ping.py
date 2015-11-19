import socket
import sys
import time

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("", 1337))

while True:
	message = ""
	message, address = server.recvfrom(1337)
	if message == "done":
		sys.exit()		
	if message != "":
		time.sleep(2)
		print("Server: Received message " + str(message) + " and sending back to client.")
		server.sendto(str(message), address)
