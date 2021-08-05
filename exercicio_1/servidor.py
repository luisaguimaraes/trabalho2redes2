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

#Estabelecendo conexão IPV4 e TCP.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  # Associa o socket a uma porta e um host.
    s.listen() # Aguardando conexão de clientes
    conn, addr = s.accept() # Aceitando conexões.
    with conn:
        while True: # Se tiver conexão...
            data = conn.recv(1024) # Recebe dados de cliente de acordo com o buffer.
            print(data) # Imprime a mensagem recebida do cliente.
            if not data: # Se não houver dados, não irá imprimir.
                break
            str = ("Oi cliente, tudo bem? Obrigado pela mensagem. Minha hora e : %s:%s" % (
            dt.datetime.now().hour, dt.datetime.now().minute))
            conn.sendall(str.encode('ascii')) # Envia resposta ao cliente.
