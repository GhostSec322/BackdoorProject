import socket

addr = ('0.0.0.0', 12345)
with socket.socket() as s:
    s.bind(addr)
    s.listen()
    print("Server Started")
    
    conn, addr = s.accept()
    print('Connect by', addr)

    while True:
        try:
            data = conn.recv(1024)
            if data:
                print(data.decode(), end='')

            data = input('>>')
            conn.send(data.encode())
        except Exception as e:
            print(e)

print("{} is disconnected".format(addr))
