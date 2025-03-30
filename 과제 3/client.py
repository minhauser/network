import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

# 서버의 환영 메시지 수신
msg = sock.recv(1024)
print(msg.decode())

# 본인의 이름을 문자열로 전송
name = "Sunnatullo"
sock.send(name.encode())

# 학번 수신 (정수형, 4바이트)
student_id_data = sock.recv(4)

# 엔디언 변환 (네트워크 바이트 순서 -> 리틀 엔디언)
student_id = struct.unpack("!I", student_id_data)[0]
print(f"학번 (엔디언 변환 후): {student_id}")

sock.close()
