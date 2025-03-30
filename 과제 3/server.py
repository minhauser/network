import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 9000))  # `blind` 오타 수정 -> `bind`
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from', addr)
    
    # 클라이언트에 환영 메시지 전송
    client.send(b'Hello ' + addr[0].encode())

    # 학생의 이름을 수신 후 출력
    name = client.recv(1024).decode()
    print("학생의 이름:", name)

    # 학번을 정수형으로 저장 후 엔디언 변환하여 전송
    student_id = 20221471
    client.send(struct.pack("!I", student_id))  # 네트워크 바이트 순서로 변환 후 전송

    client.close()
