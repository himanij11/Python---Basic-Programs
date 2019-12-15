#SERVER

import socket

def server_program():
    #get host name
    host = socket.gethostname()
    port = 5000     	#initiate port number above 1024

    server_socket = socket.socket()     #get instance
    #look closely.The bind() function takes tuple as arguement

    server_socket.bind((host,port))     #bind host address and port together

    #configure how many clients the server can listen simultaneously
    server_socket.listen(5)
    conn,address = server_socket.accept()   #accept new connection
    print("Connection from:" + str(address))
    while True:
        #receive data stream.It won't accept data packet greater than 1024
        data = conn.recv(1024).decode()
        if not data :
            #if the data is not rreceived break
            break
        print("from connected user:" +str(data))
        data = input('->')
        conn.send(data.encode())    #send the data to the client

    conn.close()    #close the connection 

server_program()
