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

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORTA))
    str = ("Sou cliente C, hora da requisicao: %s:%s" % (dt.datetime.now().hour, dt.datetime.now().minute))
    s.sendall(str.encode('ascii'))
    data = s.recv(1024)

print(repr(data))