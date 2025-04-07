import socket
import random
import time

HOST = '127.0.0.1'  # 서버 IP 주소
PORT = 5001         # 디바이스 1 포트

def generate_sensor_data():
    temperature = random.randint(0, 40)
    humidity = random.randint(0, 100)
    light = random.randint(70, 150)
    return f"{temperature},{humidity},{light}"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.sendall(generate_sensor_data().encode())
        time.sleep(3)  # 3초마다 데이터 전송
