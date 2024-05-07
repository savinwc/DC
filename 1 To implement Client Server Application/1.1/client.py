import socket

def client_program():
    host = socket.gethostname()  # Get the hostname
    port = 5000  # Same port as server

    client_socket = socket.socket()  # Get instance
    client_socket.connect((host, port))  # Connect to the server

    message = input(" -> ")  # Take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # Send message
        data = client_socket.recv(1024).decode()  # Receive response
        print('Received from server: ' + data)  # Print response
        message = input(" -> ")  # Again take input

    client_socket.close()  # Close the connection

if __name__ == '__main__':
    client_program()
