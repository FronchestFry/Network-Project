#Server

import socket

host = socket.gethostbyname(socket.gethostname()) #Since this is the server, it just hosts on whatever adress it is on. Clients will have to type the target IP
port = 1578 #Chosen arbatrarily from anything above 1000

network_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
network_object.bind((host, port))

print(f'Server launched. Clients will need to connect to the ip {host} and the port {port}.')

network_object.listen()

client_connection, client_adress = network_object.accept()

print(f"Connected to by {client_adress}")
client_connection.sendall(b"You have connected successfully")

while True:
#Echo to check connection
    #Recive data
    incoming_data = client_connection.recv(port)

    #Check that the client still exists

    if not incoming_data:
        print (f"client '{client_adress}' disconnected")
        break

    #As long as they do, send the data back

    print(f"recived '{incoming_data.decode()}'")
    outgoing_data = incoming_data + b" (but echoier)"
    client_connection.sendall(outgoing_data)
