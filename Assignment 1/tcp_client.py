import socket

HOST = "127.0.0.1"
PORT = 53333

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    client_socket.sendall("hello TCP".encode())
    data = client_socket.recv(1024).decode()
    print("Received from server:", data)
