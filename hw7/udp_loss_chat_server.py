# udp_loss_chat_server.py
from socket import *
import random
import time

# Server configuration
port = 3333
BUFF_SIZE = 1024

# Create socket
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

print("[Server Started] Waiting for messages...")

# Server loop
while True:
    sock.settimeout(None)  # blocking mode
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE)
        if random.random() <= 0.5:  # simulate 50% packet loss
            continue
        else:
            sock.sendto(b'ack', addr)
            print('<-', data.decode())
            break

    # 서버에서 클라이언트로 메시지 전송
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
