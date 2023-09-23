import json
import socket

server = socket.socket()
hostname = socket.gethostbyname(socket.gethostname())
port =45321
server.bind((hostname, port))
server.listen(1)
print(f'сервер запущен \nадрес сервера: {hostname} \nport: {port}')
con, addr = server.accept()

maps = ['', 1, 2, 3, 4, 5, 6, 7, 8, 9]
player_1 = True

data = {'maps': maps, 'player_1': player_1}


def maps_print():
    print('__________________')
    for i in range(1, len(maps), 3):
        print(f'\t{data["maps"][i]}{data["maps"][i + 1]}{data["maps"][i + 2]}')
    print('__________________')


while True:
    if data['player_1']:
        maps_print()
        print('ход первого игорка')
        hod = int(input('куда ходим?'))
        data['maps'][hod] = 'x'
        data['player_1'] = False
        data_json = json.dumps(data)
        con.send(data_json.encode())
    else:
        maps_print()
        print('ход второго игорка')
        data_json= con.recv(1024)
