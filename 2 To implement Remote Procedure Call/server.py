import socket
import pickle

# Define the function to be called remotely
def add(numbers):
    return numbers['a'] + numbers['b']

# Create a socket and bind it to a port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 5000))  # Change "localhost" to "kris"
server_socket.listen(1)
print("RPC Server listening on port 8000...")

while True:
    # Wait for a connection
    client_socket, _ = server_socket.accept()
    print("Connected to client")

    # Receive data from the client
    data = client_socket.recv(1024)
    if not data:
        break

    # Deserialize received data
    numbers = pickle.loads(data)

    # Call the remote function
    result = add(numbers)

    # Send the result back to the client
    client_socket.send(pickle.dumps(result))
    client_socket.close()

server_socket.close()
