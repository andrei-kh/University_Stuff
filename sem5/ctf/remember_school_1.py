import socket
from math import hypot

sock = socket.socket()
sock.connect(("ctf.mf.grsu.by", 9002))

while True:
    data = sock.recv(1024).decode('utf-8')
    if 'grodno{' in data:
        print(data)
        break
    if "Правильно" in data:
        continue
    numbers = map(float, data.split('\n')[-2].split(';'))
    x1, y1, x2, y2 = numbers
    result = hypot(x1 - x2, y1 - y2)
    sock.send((str(round(result, 2)) + '\r\n').encode())

sock.close()
