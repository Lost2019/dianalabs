import socket

socks = socket.socket()
socks.bind(('', 9090))
socks.listen(1) # Кол-во прослушеных соединений
rez = 'Поступившего сообщения не было'
vir1 = ' '
conn, addr = socks.accept() #Открытие соединения

print('connected:', addr)

while True:
    conn.send(rez.encode()) #Кодирует rez
    vir1 = conn.recv(1024).decode()
    if not vir1:
        break
    rez = vir1