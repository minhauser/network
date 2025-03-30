import socket
import re

def calculate(expression):
    """문자열에서 연산자를 파싱하고 계산을 수행"""
    match = re.match(r'(\d+)([+\-*/])(\d+)', expression)
    if not match:
        return "오류: 잘못된 입력 형식입니다."

    num1, operator, num2 = match.groups()
    num1, num2 = int(num1), int(num2)

    if operator == '+':
        return str(num1 + num2)
    elif operator == '-':
        return str(num1 - num2)
    elif operator == '*':
        return str(num1 * num2)
    elif operator == '/':
        if num2 == 0:
            return "오류: 0으로 나눌 수 없습니다."
        return f"{num1 / num2:.1f}"  

def main():
    server_address = ('localhost', 9000)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(server_address)
        server.listen(5)
        print("서버가 실행되었습니다. (클라이언트 연결 대기 중...)")

        while True:
            client, addr = server.accept()
            print(f"클라이언트 연결됨: {addr}")

            with client:
                while True:
                    data = client.recv(1024).decode()
                    if not data:
                        break

                    result = calculate(data) 
                    client.sendall(result.encode())  

if __name__ == "__main__":
    main()
