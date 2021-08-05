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
            data = conn.recv(1024) # Recebe dados de acordo com o buffer. Neste caso, 1024 bits.
            if not data:
                break
            print(data) #Imprime dados da requisição.
            str = ("hora de antendimento: %s:%s" % (dt.datetime.now().hour, dt.datetime.now().minute))
            conn.sendall(str.encode('ascii')) # Envia resposta ao cliente.

# definindo servidor e porta.
HOST = '127.0.0.1'
PORTA = 65432

#Estabelecendo conexão IPV4 e TCP.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORTA)) # Associa um host a uma porta.
    threads = [] # Instanciando uma lista de threads.

    while True:
        s.listen(4) # Deixa o socket aberto aguardando conexões.
        print("server up") # Retorno caso haja conexão, confirmando que o servidor está ok.
        conn, addr = s.accept() # Aceitando conexão.
        n_thread = ThreadCliente(addr) # Inicia endereço de cada cliente.
        n_thread.start() # Startando a thread.
        threads.append(n_thread) # Dando sequência a lista de clientes
