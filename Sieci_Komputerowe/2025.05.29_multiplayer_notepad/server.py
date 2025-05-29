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

    if data[0:1] == b"\1":
        print("- get message package")
        message = data[1:]

        print(users)

        if addr in users.keys():
            for user in users.keys():
                sock.sendto(users[user] + b": " + message, user)
            
            print("- send to all users")



    # print(f"received message: {data}")