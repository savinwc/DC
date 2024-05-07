import socket
import threading
def handle_client(client_socket, client_address):
    print(f"Accepted connection from {client_address}")
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Received from {client_address}: {data}")
        client_socket.send(data.encode())
    client_socket.close()
    print(f"Connection with {client_address} closed")
def server_program():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)

    print("Server started, waiting for connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connected to {client_address}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == '__main__':
    server_program()