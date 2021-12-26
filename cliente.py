#criando a parte do cliente
import socket

HOST='localhost'
#HOST = '127.0.0.1'
PORT = 50000

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#pedindo conexão
s.connect((HOST, PORT))
#enviar dados
s.sendall(str.encode('Está conectano'))
#Gravando dados
data=s.recv(1024)

print('Conexão estabelecida', data.decode())

