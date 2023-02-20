import socket
import time 
import datetime
import uuid

website = 'www.example.com'
#proxy server and port
proxy_port = 8901
proxy_host = str(socket.gethostbyname(socket.gethostname()))

#socket the client will use to communicate with the proxy server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((proxy_host,proxy_port))

time1 = time.time()

#website= input("Enter the website ip you want to access: ")
request = messagetosend=f"GET http://{website}/HTTP/1.1\r\nHost:{website}\r\n\r\n"
client_socket.sendall(request.encode())#send the clients request to the proxy server which will process the request and send to main destination
print("Requesting to go to: "+ website)

#response from proxy server
response = client_socket.recv(1024).decode()#receiving response from proxy server about the previous request
time2=time.time()
print("The response is: "+ response)


mac = uuid.getnode()

client_socket.close()
time2 = time.time()

print("elapsed time is: ", time2-time1,"seconds.\nthe mac address is: "+ hex(mac))
