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
            print(self.data) # Imprime os dados recebidos do cliente.
            str = ("hora de antendimento: %s:%s" % (dt.datetime.now().hour, dt.datetime.now().minute))
            s.sendto(str.encode('ascii'), (self.host, self.porta)) # enviando resposta para o cliente.
            break


# definindo servidor e porta.
HOST = '127.0.0.1'
PORTA = 65431

#Estabelecendo conexão IPV4 e UDP.
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORTA)) # Associa o socket a um host e uma porta específica.
    threads = [] # Buscando a thread de clientes.

    while True:
        data = s.recvfrom(1024) # Recebe dados de acordo com o tamanho do buffer. (Nesse caso, 1024 bits)
        n_thread = ThreadCliente(data[1][0], data[1][1], data[0])
        n_thread.start() # Startando a thread.
        threads.append(n_thread) # Associa uma thread a um cliente