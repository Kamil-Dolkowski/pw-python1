import socket

users = {}

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)

    print("\n===== New message =====")

    if data[0:1] == b"\0":
        print("- get nickname package")
        nickname = data[1:]

        if nickname not in users.values():
            users[addr] = nickname
            print("- add new nickname")
        else:
            print("- nickname already exists")

    elif data[0:1] == b"\1":
        print("- get message package")
        message = data[1:]

        if addr in users.keys():
            for user in users.keys():
                sock.sendto(users[addr] + b": " + message, user)
            
            print("- send to all users")

    elif addr in users.keys():
        nickname = users[addr]
        print(f"- disconnect user with nickname {nickname}")

        del users[addr]
        print(f"- delete user with nickname {nickname}")

    else:
        print("- ignore message")

# sock.close()