import socket
import time

HOST = "127.0.0.1"
PORT = 53333

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print("Connected to TCP server.")

    client_socket.sendall("hello TCP".encode())
    data = client_socket.recv(1024).decode()
    print("Server:", data)

    while True:
        time.sleep(1)
