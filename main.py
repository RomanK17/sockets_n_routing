import socket

def run():
    """серверная часть, обрабатывает запросы"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 3009))
    server_socket.listen()

    print("сервер слушаем по порту 3009")
    while True:
        client_socket, adress = server_socket.accept() # получаем сокет клиента
        request = client_socket.recv(1024) # получаем данные из запроса

        print(request)

        print(adress)

        client_socket.sendall("hello".encode()) # кодируем в байты, тк общаемся байтами

        client_socket.close()

if __name__ == '__main__':
    run()