'''Trabalho Prático 2.
Grupo:
Alessandro Luís Moreira.
Gabriele Iara Ferreira.
Luísa Vitória Guimarães Silva.
Taylon Higor Pinheiro Costa.
Tiago Mercês Rosário. '''

from threading import Thread # importação da biblioteca que permite threads, permitem aplicações rodando em paralelo.
import socket  # importação da biblioteca de conexão.
import datetime as dt  # importação da biblioteca de horas.

class ThreadCliente(Thread):
# Criando a thread de clientes, para processar mais de um cliente em paralelo.
    def __init__(self, addr):
        Thread.__init__(self)
        self.host = addr[0]
        self.porta = addr[1]
        print("Nova conexao de " + str(self.host) + ", na porta " + str(self.porta))

    def run(self):
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data)
            str = ("hora de antendimento: %s:%s" % (dt.datetime.now().hour, dt.datetime.now().minute))
            conn.sendall(str.encode('ascii'))

# definindo servidor, porta e recebimento de dados antes de execução.
HOST = '127.0.0.1'
PORTA = 65432
BUFFER = 1024

#Estabelecendo conexão TCP.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORTA))
    threads = [] # Buscando a thread de clientes.

    while True:
        s.listen(4) # Definição de quantas aplicações estão rodando.
        print("server up") #Retorno caso haja conexão.
        conn, addr = s.accept() # Aceitando conexão.
        n_thread = ThreadCliente(addr) # Buscando endereço de cada cliente.
        n_thread.start() # Startando a thread.
        threads.append(n_thread) # Dando sequência a lista de clientes
