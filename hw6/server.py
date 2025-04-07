import socket
import threading

# 서버 함수 정의 (이 코드가 있어야 합니다!)
def socket_server(port, device_name):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(5)
    print(f"{device_name} 서버 실행 중... (포트 {port})")

    while True:
        client_socket, addr = server_socket.accept()
        data = client_socket.recv(1024).decode('utf-8')
        with open("data.txt", "a") as f:
            f.write(data + "\n")
        print(f"{device_name} 데이터 수신: {data}")
        client_socket.close()

# 스레드 실행
ports = [5001, 5002]  # 두 개의 디바이스 포트
for i, port in enumerate(ports):
    threading.Thread(target=lambda: socket_server(port, f"Device{i+1}")).start()
