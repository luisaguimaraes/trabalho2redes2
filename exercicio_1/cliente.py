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
PORT = 65432

# Estabelecendo conexão IPV4 e TCP.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) # Inicia conexão.
    str = ("Oi servidor, tudo bem? Minha hora e: %s:%s" % (dt.datetime.now().hour, dt.datetime.now().minute)) # Mensagem a ser exibida após a conexão.
    s.sendall(str.encode('ascii')) # Envia mensagem ao servidor.
    data = s.recv(1024) # Recebe dados de acordo com o buffer.

print(repr(data)) # Imprime mensagem recebida.