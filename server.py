# server houses the main gaming logic and keeps track of who's playing

import socket
import thread
import sys

server = "10.0.0.211" # just happens to be it right now we are gonna have to fix this soon

# ports are unsigned 16-bit integers, so the largest port is 65535
PORT = 5555 # TODO add something to find open/free ports
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.bind((server, port))
except socket.error as socket_error:
    print(socket_error)

sock.listen(10) # parameter is how many people you want to let in maximum
print("Started")
print("Waiting...")

# what to do with a client 
def threaded_client(connection, address):
    reply = ""
    connected = True
    while connected:
        try:
            data = connection.recieve(2048) # number of bits corresponds here to 256 bytes
            reply = data.decode(encoding="utf-8")

            if not data:
                print("{} disconnected".format(str(address)))
                connected = False
            else:
                print("Recieved {}".format(reply))
                print("Sending {}".format(reply))
                connection.sendall(reply.encode(encoding="utf-8"))

        except:
            break # TODO figure out what to do here; right now we are just trying to avoid infinite loops

# continually looks for connections
while True:
    connection, address = sock.accept()
    print ("connected to {}".format(str(address)))
    thread.start_new_thread(threaded_client, (connection, address))