import socket

def main():
    server_address = ('localhost', 9000)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(server_address)
        print("계산기 서버에 연결되었습니다. (종료하려면 'q' 입력)")

        while True:
            expr = input("계산식을 입력하세요 (예: 20+17): ").replace(" ", "")  # 공백 제거
            if expr.lower() == 'q':
                break

            sock.sendall(expr.encode())  
            result = sock.recv(1024).decode()  
            print(f"결과: {result}")

    print("연결이 종료되었습니다.")

if __name__ == "__main__":
    main()
