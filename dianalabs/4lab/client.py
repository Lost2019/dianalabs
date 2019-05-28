import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
while True:
	mission = input('Введите строку: ')
	sock.send(mission.encode()) # Кодируеи в байт 
	answer= sock.recv(1024).decode() #Принимает ответ и декодирует
	print('Результат работы сервера: ', answer)
sock.close()
