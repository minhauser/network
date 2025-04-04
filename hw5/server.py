import socket
import os

HOST = "127.0.0.1"
PORT = 80
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"웹 서버 실행 중: http://{HOST}/")

while True:
    client_socket, addr = server_socket.accept()
    print(f"클라이언트 연결됨: {addr}")

    request = client_socket.recv(1024).decode()
    print(f"클라이언트 요청:\n{request}")

    if not request:
        client_socket.close()
        continue

    first_line = request.split("\n")[0]
    requested_file = first_line.split(" ")[1]

    if requested_file == "/":
        requested_file = "/index.html"

    filename = requested_file.lstrip("/")
    filepath = os.path.join(BASE_DIR, filename)
    
    if os.path.exists(filepath):
        if filename.endswith(".html"):
            mime_type = "text/html"
            with open(filepath, "r", encoding="utf-8") as f:
                response_body = f.read()
            response_data = response_body.encode("utf-8")
        elif filename.endswith(".png"):
            mime_type = "image/png"
            with open(filepath, "rb") as f:
                response_data = f.read()
        elif filename.endswith(".ico"):
            mime_type = "image/x-icon"
            with open(filepath, "rb") as f:
                response_data = f.read()
        else:
            mime_type = "application/octet-stream"
            with open(filepath, "rb") as f:
                response_data = f.read()

        response_headers = (
            "HTTP/1.1 200 OK\r\n"
            f"Content-Type: {mime_type}\r\n"
            f"Content-Length: {len(response_data)}\r\n"
            "Connection: close\r\n"
            "\r\n"
        ).encode("utf-8")

        client_socket.send(response_headers + response_data)

    else:
        response_body = "<html><head><title>Not Found</title></head><body><h1>404 Not Found</h1></body></html>"
        response_headers = (
            "HTTP/1.1 404 Not Found\r\n"
            "Content-Type: text/html\r\n"
            f"Content-Length: {len(response_body)}\r\n"
            "Connection: close\r\n"
            "\r\n"
        ).encode("utf-8")

        client_socket.send(response_headers + response_body.encode("utf-8"))

    client_socket.close()
