import socket
from views import index, hello


URLS = {"/":  index, "/hello" : hello}


def generate_headers(method, url):
    if not method == "GET":
        return ("HTTP/1.1 405 Method not allowed\n\n", 405)
    if url not in URLS:
        return ("HTTP/1.1 404 Not found\n\n", 404)
    return ("HTTP/1.1 200 OK\n\n", 200)


def parse_request(request):
    parsed = request.split(" ")
    return parsed[0], parsed[1]


def generate_body(code, url):
    if code == 404:
        return "<h1>404</h1><p>Method not allowed</p>"
    if code == 405:
        return "<h1>405</h1><p>Not found</p>"
    if code == 200:
        return URLS[url]()


def generate_response(request):
    method, url = parse_request(request)
    headers, status_code = generate_headers(method, url)
    body = generate_body(status_code, url)
    return (headers + body).encode()


def run():
    """серверная часть, обрабатывает запросы"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(
        socket.SOL_SOCKET, socket.SO_REUSEADDR, 1
    )  # убираем задержку при закрытии порта
    server_socket.bind(("localhost", 3009))
    server_socket.listen()

    print("сервер слушаем по порту 3009")
    while True:
        client_socket, adress = server_socket.accept()  # получаем сокет клиента
        request = client_socket.recv(1024)  # получаем данные из запроса

        print(request)

        print(adress)

        response = generate_response(request.decode("utf-8"))

        client_socket.sendall(response)  # кодируем в байты, тк общаемся байтами

        client_socket.close()


if __name__ == "__main__":
    run()
