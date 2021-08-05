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

#Estabelecendo conexão UDP.
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

    str = ("Oi servidor, tudo bem? Minha hora e: %s:%s" % (dt.datetime.now().hour, dt.datetime.now().minute))
    s.sendto(str.encode('ascii'), (HOST, PORT)) # Convertendo a mensagem para ser recebido no formato ASCII.
    data, addr = s.recvfrom(1024) # Recebendo mensagem e endereço e verificando a conexão.

print(data)
