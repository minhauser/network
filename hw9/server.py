import socket
import select

HOST = '127.0.0.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"서버 시작: {HOST}:{PORT}")

socket_list = [server_socket]
clients = {}  # 소켓: 이름


def broadcast(sender_socket, message):
    for client_socket in clients:
        if client_socket != sender_socket:
            try:
                client_socket.send(message)
            except BaseException:
                client_socket.close()
                socket_list.remove(client_socket)
                del clients[client_socket]


while True:
    read_sockets, _, exception_sockets = select.select(
        socket_list, [], socket_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            name = client_socket.recv(1024).decode()
            socket_list.append(client_socket)
            clients[client_socket] = name
            print(f"새 연결: {name} from {client_address}")
        else:
            try:
                message = notified_socket.recv(1024)
                if not message:
                    continue

                if message.strip().decode().lower() == 'quit':
                    print(f"{clients[notified_socket]} 연결 종료")
                    socket_list.remove(notified_socket)
                    del clients[notified_socket]
                    notified_socket.close()
                else:
                    name = clients[notified_socket]
                    full_message = f"[{name}] {message.decode()}"
                    print(full_message.strip())
                    broadcast(notified_socket, full_message.encode())
            except BaseException:
                socket_list.remove(notified_socket)
                notified_socket.close()
                del clients[notified_socket]

    for notified_socket in exception_sockets:
        socket_list.remove(notified_socket)
        notified_socket.close()
        del clients[notified_socket]
