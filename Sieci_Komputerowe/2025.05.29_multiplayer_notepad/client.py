import socket
import select
import sys

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.setblocking(False)

nickname = bytes(input("Nickname: "), "utf-8")

if len(nickname) > 0:
    nickname = b"\0" + nickname
    sock.sendto(nickname, (UDP_IP, UDP_PORT))

try:
    while True:
        read_list = [sock, sys.stdin]
        read, _, _ = select.select(read_list, [], [])

        for s in read:
            if s is sys.stdin:
                message = bytes(input(), "utf-8")

                if message == b"":
                    message = b""
                    sock.sendto(message, (UDP_IP, UDP_PORT))

                    print("\nDisconnected with server")

                    sock.close()
                    sys.exit(0)
                else:
                    message = b"\1" + message
                    sock.sendto(message, (UDP_IP, UDP_PORT))

            if s is sock:
                data, addr = sock.recvfrom(1024)

                if data == b"Error: Nickname already exists":
                    print("\nThis nickname already exists")
                    print("Disconnected with server")

                    sock.close()
                    sys.exit(0)
                else:
                    print(f"-{data.decode("utf-8")}")

    # sock.close()

except KeyboardInterrupt:
    sock.sendto(b"", (UDP_IP, UDP_PORT))
    
    sock.close()
    print("\nDisconnected with server")