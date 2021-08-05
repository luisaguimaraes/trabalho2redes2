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

# Conexão UDP.
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

    s.bind((HOST, PORT)) # Iniciando a conexão, escolhendo qual host e qual porta vão ser conectadas.

    while True:
        
        s.settimeout(5.0) # Tempo de conexão ao servidor.
        data = s.recvfrom(1024) # Retorno da conexão.

        if not data:
            break

        str = ("Oi cliente, tudo bem? Obrigado pela mensagem. Minha hora e : %s:%s" % (dt.datetime.now().hour, dt.datetime.now().minute))
        # Mensagem de retorno da conexãoa bem sucedida.

        s.sendto(str.encode('ascii'), (data[1][0], data[1][1]))

        print(data[0])