import socket
import datetime
#proxy server and port
proxy_port = 13103
proxy_host = str(socket.gethostbyname(socket.gethostname()))

#server address and port
server_port= 80
hostname = socket.gethostbyname('www.example.com')


#creating socket 
#this socket is just for the proxy server to accept connections not for communications
proxy_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

#binding the socket to my address to be able to host
proxy_socket.bind((proxy_host,proxy_port))

#socket.listen allows server to listen to incoming connections 
proxy_socket.listen()


while True: 
    #when a client tries to connect to server,
    #the 'accept' method triggers and returns address of
    #the client that is connecting and a socket we can use 
    #to commincate with client
    comm_socket = proxy_socket.accept()
    address = proxy_socket.accept()
    print("Successfully connected to " + address +"at a time of: "+datetime.datetime.now())
    #receive clients request
    request = comm_socket.recv(1024).decode()
    print("received request: " +request+ ", from client of address: " +address )
    ip = address.split()[1].split('')[2] #destination ip address

    #now we would like to connect to the target server
    #we start off by creating socket 
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #connect to target server
    server_socket.connect((ip,server_port))
    #we send http request to server host
    server_socket.sendall(request.encode())
    print("request sent at time: "+ datetime.datetime.now())

    #now we receive response from server
    response = server_socket.recv(1024).decode()
    print('The response has been received at a time of: '+ datetime.datetime.now())

    #SEND response back to client
    comm_socket.sendall(response.encode())
    print("The response has been sent to client at a time of: "+ datetime.datetime.now())
    comm_socket.close()
    server_socket.close()

if False:
    print("error")
proxy_socket.close()
