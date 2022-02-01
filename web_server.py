# import socket module
from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
SP = 45678
# TASK 1
# Fill in start
serverSocket.bind(('', SP))
serverSocket.listen(1)
# Fill in end

while True:
    # Establish the connection
    print('Ready to serve...')

    # TASK 2
    connectionSocket, addr = serverSocket.accept()

    try:

        # TASK 3
        # Fill in start
        message = connectionSocket.recv(1024)
        print(message, message.split()[0], message.split()[1])

        filename = message.split()[1]
        f = open(filename[1:])
        # Fill in end

        # TASK 4
        # Fill in start
        output_data = f.read()
        print(output_data)
        # Fill in End

        # TASK 5
        # Send one HTTP header line into socket
        # Fill in start
        connectionSocket.send(str.encode('\nHTTP/1.1 200 OK\n\n'))
        connectionSocket.send(str.encode(output_data))

        for i in range(0, len(output_data)):
            connectionSocket.send(str.encode(output_data[i]))

        # Fill in end

        # Send the content of the requested file to the client
        for i in range(0, len(output_data)):
            connectionSocket.send(str.encode(output_data[i]))
        connectionSocket.send(str.encode("\r\n"))
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill in Start
        connectionSocket.send(str.encode('HTTP/1.1 404 Not Found\n\n'))
        #

        # TASK 7
        # Close client socket
        # Fill in start
        break
connectionSocket.close()
serverSocket.close()
# Fill in end
sys.exit()  # Terminate the program after sending the corresponding data