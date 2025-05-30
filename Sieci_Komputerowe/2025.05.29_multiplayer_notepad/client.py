import socket
import select
import sys

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.setblocking(False)

nickname = b"\0Kamil"
sock.sendto(nickname, (UDP_IP, UDP_PORT))

message = b"\1Message"
sock.sendto(message, (UDP_IP, UDP_PORT))

message = b""
sock.sendto(message, (UDP_IP, UDP_PORT))

while True:
    read_list = [sock, sys.stdin]
    read, _, _ = select.select(read_list, [], [])

    if read is sys.stdin:
        print("stdin")

    if read is sock:
        print("sock")
        data = ""
        sock.recvfrom(data)

        print(f"data: {data}")

    
    