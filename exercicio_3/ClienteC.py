'''Trabalho Prático 2.
Grupo:
Alessandro Luís Moreira.
Gabriele Iara Ferreira.
Luísa Vitória Guimarães Silva.
Taylon Higor Pinheiro Costa.
Tiago Mercês Rosário. '''

import socket  # importação da biblioteca de conexão.
import datetime as dt  # importação da biblioteca de horas.

# definindo servidor e porta.
HOST = '127.0.0.1'
PORTA = 65432

# Estabelecendo conexão IPV4 e TCP.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORTA))
    str = ("Sou cliente C, hora da requisicao: %s:%s" % (dt.datetime.now().hour, dt.datetime.now().minute))
    s.sendall(str.encode('ascii'))  # Envia a requisição ao servidor.
    data = s.recv(1024)  # Recebe a resposta do servidor.

print(repr(data))  # Imprime os dados da resposta.