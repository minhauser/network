# udp_loss_chat_client.py
from socket import *
import time
import random

# Client configuration
server_ip = '127.0.0.1'
port = 3333
BUFF_SIZE = 1024

# Create socket
sock = socket(AF_INET, SOCK_DGRAM)
addr = (server_ip, port)

print("[Client Started] Type messages to send:")

while True:
    # 클라이언트에서 서버로 메시지 전송
    msg = input('-> ')
    reTx = 0
    while reTx <= 5:
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), addr)
        sock.settimeout(2)
        try:
            data, _ = sock.recvfrom(BUFF_SIZE)
        except timeout:
            reTx += 1
            print(f"재전송 중... ({reTx}회)")
            continue
        else:
            print("ACK 수신 완료!")
            break

    # 서버 메시지 수신
    sock.settimeout(None)
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE)
        if random.random() <= 0.5:
            continue
        else:
            sock.sendto(b'ack', addr)
            print('<-', data.decode())
            break
