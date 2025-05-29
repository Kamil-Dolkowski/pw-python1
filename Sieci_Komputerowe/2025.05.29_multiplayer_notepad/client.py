import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.setblocking(False)

nickname = b"\0Kamil"
message = b"\1Message"

sock.sendto(nickname, (UDP_IP, UDP_PORT))

sock.sendto(message, (UDP_IP, UDP_PORT))