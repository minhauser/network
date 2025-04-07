import socket
import random
import time

HOST = '127.0.0.1'  # 서버 IP 주소
PORT = 5002         # 디바이스 2 포트

def generate_sensor_data():
    heartbeat = random.randint(40, 140)
    steps = random.randint(2000, 6000)
    calories = random.randint(1000, 4000)
    return f"{heartbeat},{steps},{calories}"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.sendall(generate_sensor_data().encode())
        time.sleep(3)  # 3초마다 데이터 전송
