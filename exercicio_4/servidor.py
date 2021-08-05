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

class ThreadCliente(Thread): # Criando a thread de clientes, para processar mais de um cliente em paralelo.

    def __init__(self, host, porta, data):
        Thread.__init__(self)
        self.host = host
        self.porta = porta
        self.data = data
        print("Nova conexao de " + str(self.host) + ", na porta " + str(self.porta)) # Imprimindo a nova conexão.

    def run(self):
        while True:
            if not self.data:
                break
            print(self.data)
            str = ("hora de antendimento: %s:%s" % (dt.datetime.now().hour, dt.datetime.now().minute))
            s.sendto(str.encode('ascii'), (self.host, self.porta)) # enviando requisição em Ascii.
            break


# definindo servidor, porta e recebimento de dados antes de execução.
HOST = '127.0.0.1'
PORTA = 65431
BUFFER = 1024

#Estabelecendo conexão TCP.
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORTA))
    threads = [] # Buscando a thread de clientes.

    while True:
        data = s.recvfrom(1024) #Retorno da conexão.
        n_thread = ThreadCliente(data[1][0], data[1][1], data[0])
        n_thread.start() # Startando a thread.
        threads.append(n_thread) # Dando sequência a lista de clientes