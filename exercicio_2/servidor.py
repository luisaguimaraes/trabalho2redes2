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

# Estabelecendo conexão IPV4 e UDP.
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

    s.bind((HOST, PORT)) # Associa o socket a uma porta e um host.

    while True:
        
        s.settimeout(5.0) # Tempo limite pra receber uma conexão.
        data = s.recvfrom(1024) # Recebe dados do cliente de acordo com o buffer.

        if not data:
            break

        str = ("Oi cliente, tudo bem? Obrigado pela mensagem. Minha hora e : %s:%s" % (dt.datetime.now().hour, dt.datetime.now().minute))
        # Mensagem de retorno da conexão bem sucedida.

        s.sendto(str.encode('ascii'), (data[1][0], data[1][1])) # Envia a resposta ao cliente.

        print(data[0]) # Imprime a mensagem recebida pelo cliente.