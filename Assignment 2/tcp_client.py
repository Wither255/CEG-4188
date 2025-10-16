import socket
import time

HOST = "127.0.0.1"
PORT = 53333

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print("Connected to TCP server.")
    
    start_time = time.perf_counter() # timer starts 
    
    client_socket.sendall("hello TCP".encode())
    data = client_socket.recv(1024).decode()
    
    end_time = time.perf_counter() # timer stops
    
    rtt = (end_time - start_time) * 1000  # RTT in milliseconds
    print("Server:", data)
    print(f"RTT: {rtt:.3f} ms")

    while True:
        time.sleep(1)
