import sys
import socket
import select
#from thread import *
#seridor chat 
### Author: yazalde Felimone pinto ####
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

#verificado se temos todas informacoes!
if len(sys.argv) != 3:
    print("[×]Yazalde[×]==>>> Entre com chat_server Ip port")
    exit()


#Primeiro vamos receber o IP
Ip_indress = str(sys.argv[1])

#segundo a porta!
Port= int(sys.argv[2])

'''a que vamos conectar a uma porta e a um ip'''
server.bind((Ip_indress, Port))
#vamos escolher quantas conexcoes quermos
server.listen(50)

'''vamos guardar o cliente a qui'''
list_clints = []

nikes={'admim':'admim'}

def clintth(conn, addr):
    '''Vamos enviar mensagem para o novo cliente conectado'''
    nome=(nikes[conn])
    conn.send(f"[✓]Author:Yazalde Felimone[+]=>> Bem vindo {nome}")
    while True:
        try:
            mensagem = conn.recv(2048)
            if mensagem:
                '''Mostrar a mensagem  e o nome no outro usuario'''
                print("[=>Autor:Yazalde]<✓"+addr[0]+""+nikes[conn]+"✓>"+mensagem)
                '''manadar mensagem a todas conecxoes'''
                mensagem_send=("[=>Author:Yazalde]<✓"+nikes[conn]+"✓>"+mensagem)
                broadcast(mensagem_send, conn)
            else:
                '''A posiblilidade de nao entrar a mensagem pra todos infilismente nao encotrei outra opcao alem dessa'''
                #desconectar a pessoa que nao recebe a mensagem
                remove(conn)
        except:
            continue



def broadcast(mensagem,conecoes):
    for clint in list_clints:
        if clint != conecoes:
            try:
                client.send(mensagem)
            except:
                client.close()
                ##banicao do clinete do chat
            remove(client)

def remove(conecoes):
    if conecoes in list_clints:
        list_clints.remove(conecoes)

while True:
    '''receber as conecaoes no meio da coversa'''
    conn, addr = server.accept()
    nik = conn.recv(2048)
    '''colocar a nova pessoa na coversa no chat'''
    list_clints.append(conn)
    ''''verificar se o nome do nove ja nak exit nas pessoas conectadas '''
    t = True
    for i in nikes:
        if nikes[i] == nik :
            t = True
        else:
            t = False
    #verificar a se o server esta disponiveo
    if t == False:
        nikes[conn] = nik
        '''envio de cofirmacao ao cliente'''
        conn.send("1")
    #se nao estiver disponivel enviamos ao servidor essa negacao
    else:
        while t:
            conn.send("0")
            nik = conn.recv(2048)
            if nikes[i] == nik:
                t = True
            else:
                t = False
                nikes[conn] = nik
                conn.send("1")
        '''premir a a conexcao do novo usuario'''
        print("[✓]Author:Yazalde[✓]=>>"+ addr[0]+ " " +nik+ "sucesso na conexcao")
        '''vou criar um prosseco individual pra cada client novo na rede'''
        start_new_thread(clientthread,(conn,addr))

conn.close()
servidor.close()
start_new_thread.close()
