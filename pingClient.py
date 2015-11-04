import socket
import time
import sys

UDP_IP = "127.0.0.1"
UDP_PORT = 1337
data = "DATA"

#server = raw_input("Enter a website: ")
#try:
#	server = socket.gethostbyname(server)
#	print("Server IP is " + server)
#except:
#	print("Trouble getting ip. Perhaps website entered incorrectly?")
#	sys.exit()

sendingSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sendingSocket.settimeout(1)

i = 1
while i <= 10:
	start = time.time() 
	sendingSocket.sendto(data + " " + str(i), (UDP_IP, UDP_PORT))
	print "Client: Sending data containing contents: " + data + " " + str(i)
	i = i+1
	returnedData, server = sendingSocket.recvfrom(1337)
	print("Client: Received back message: " + returnedData)
	rtt = time.time() - start
	print("Elapsed time in seconds = " + str(rtt) + "seconds.")
	time.sleep(0.5)
print("Done!")

sendingSocket.sendto("done", (UDP_IP,UDP_PORT))
