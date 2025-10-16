import socket
import time

HOST = "127.0.0.1"
PORT = 53444

NUM_MESSAGES = 1000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    print(f"Connected to UDP server. Sending {NUM_MESSAGES} messages...")


    start_time = time.perf_counter()

    for i in range(NUM_MESSAGES):
        client_socket.sendto(b"hello UDP", (HOST, PORT))


    data, _ = client_socket.recvfrom(1024)
    end_time = time.perf_counter()

    total_time = (end_time - start_time) * 1000  # RTT in ms
    print("Server:", data.decode())
    print(f"Total time for {NUM_MESSAGES} messages: {total_time:.3f} ms")
    print(f"Average per message: {total_time / NUM_MESSAGES:.6f} ms")

    while True:
        time.sleep(1)
