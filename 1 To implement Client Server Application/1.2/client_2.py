import socket

def client_program():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    while True:
        message = input("Client 1: Enter message: ")
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print('Received from server: ' + data)
        if message.lower().strip() == 'bye':
            break

    client_socket.close()

if __name__ == '__main__':
    client_program()
