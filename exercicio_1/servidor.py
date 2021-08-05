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

# Criando socket para criar a conexão cliente-servidor.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  # Mostrando qual host e qual porta irão fazer conexão.
    s.listen() # Mostrando quantas conexões irão enfileirar, neste caso, quantas requisições forem precisas.
    conn, addr = s.accept() # Aceitando conexões.
    with conn:
        while True: # Se tiver conexão...
            data = conn.recv(1024)
            print(data) # Imprime o horário.
            if not data: # Se não houver conexão, não irá imprimir.
                break
            str = ("Oi cliente, tudo bem? Obrigado pela mensagem. Minha hora e : %s:%s" % (
            dt.datetime.now().hour, dt.datetime.now().minute)) # Mensagem que será exibida na tela, caso encontre conexão.
            conn.sendall(str.encode('ascii'))
