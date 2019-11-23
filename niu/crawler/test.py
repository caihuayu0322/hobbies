import socket
import threading

CONFIG_BUFSIZE_MAX = 1048576

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('114.118.10.233', 3050))

sock.send(bytes.fromhex('0400000701f21000387b7d'))


def receive_print():
    while True:
        try:
            data = sock.recv(CONFIG_BUFSIZE_MAX)
            print(1)
            print(data)
        except Exception as e:
            print(e)


threading.Thread(target=receive_print, daemon=True).start()
sock.send(bytes.fromhex('0400000701f21000387b7d'))
