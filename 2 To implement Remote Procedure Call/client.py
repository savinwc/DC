import socket
import pickle

# Function to call the RPC server
def add_prog(host, x, y):
    
    # Create a socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 5000))  # Change "localhost" to "kris"

    # Prepare data to be sent
    numbers = {'a': x, 'b': y}
    data = pickle.dumps(numbers)

    # Send data to the server
    client_socket.send(data)

    # Receive result from the server
    result = client_socket.recv(1024)

    # Deserialize received data
    result = pickle.loads(result)

    print("Result:", result)

    client_socket.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 4:
        print("Usage: {} server_host x y".format(sys.argv[0]))
        sys.exit(1)
    add_prog(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
