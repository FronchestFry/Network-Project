#Client

import socket

server_addr = input("Server IP:\n")
server_port = int(input("Server Port:\n"))

#Make the object that interacts with networks
network_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Connect to the server
network_object.connect((server_addr, server_port))

print (network_object.recv(server_port).decode())

while not network_object._closed:
    #print recived data
    incoming_data = network_object.recv(server_port)
    print(f"Opponent Returned Fire at '{incoming_data.decode()}'")

    #Get an input and send it to whomever I'm connected to
    outgoing_data = input("Awaiting attack cordinates:\n")
    if outgoing_data.lower() == "quit":
        network_object.close()
    else:
        print(f"Shot fired at '{outgoing_data}'. Awaiting enemy's return fire.")
        network_object.sendall(outgoing_data.encode())
