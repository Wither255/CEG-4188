import socket
import time

HOST = "127.0.0.1"
PORT = 53444

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    print("Connected to UDP server.")


    start_time = time.perf_counter() # Timer starts
    
    client_socket.sendto(b"hello UDP", (HOST, PORT))
    data, _ = client_socket.recvfrom(1024)
    
    end_time = time.perf_counter()  # Timer ends

    rtt = (end_time - start_time) * 1000  # RTT in milliseconds
    print("Server:", data.decode())
    print(f"RTT: {rtt:.3f} ms")

    while True:
        time.sleep(1)
