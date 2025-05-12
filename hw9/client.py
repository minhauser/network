import socket
import threading

HOST = '127.0.0.1'
PORT = 12345


def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024)
            if not message:
                break
            print(f"\n{message.decode()}")
        except BaseException:
            break


def main():
    name = input("당신의 이름을 입력하세요: ")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # 서버에 이름 전송
    client_socket.send(name.encode())

    print("서버에 연결되었습니다. 'quit' 입력 시 종료됩니다.")

    # 수신 쓰레드 시작
    threading.Thread(
        target=receive_messages,
        args=(
            client_socket,
        ),
        daemon=True).start()

    while True:
        msg = input()
        client_socket.send(msg.encode())
        if msg.strip().lower() == 'quit':
            break

    client_socket.close()


if __name__ == "__main__":
    main()
