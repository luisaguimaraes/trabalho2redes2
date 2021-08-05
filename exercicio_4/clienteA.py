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

#Estabelecendo conexão IPV4 e UDP.
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

    str = ("Cliente A, hora da requisicao: %s:%s" % (dt.datetime.now().hour, dt.datetime.now().minute))
    s.sendto(str.encode('ascii'), (HOST, PORTA)) # Envia a requisição ao servidor.
    data, addr = s.recvfrom(1024) # Recebe a resposta do servidor.

print(data) #Imprime os dados da resposta.
