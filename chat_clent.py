import socket
import select
import sys



'''criado o servidor do clinte'''
servidor=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
'''verificado os dandos nessesarios do servidor'''
if len(sys.argv) != 3:
    print("[✓]Author:Yazalde[✓]=>>> Ente com chat_clent.py Ip porta")
    exit()
Ip_address = str(sys.argv[1])
Port = int(sys.argv[2])
'''Fazendo a conexcao com o Ip e a porta ao servidor'''
servidor.connect((Ip_address, Port))
nik = input("[✓]Author:Yazalde[✓]=>> Entre com o teu nome: ")
print("\n")
'''Vou enviar o nome para o servidor'''
servidor.send(nik)
'''receber a informacao do sevidor se aceitou a conecao ou nao'''
truck = servidor.recv('1')
'''verificar se a pessoaa digitou alguma coisa no nome ou nao e verificacao se o nome existe'''
while (truck == "0"):
    nik=input("\n[×]Author:Yazalde[×]=>> Este nome ja existe tente outro")
    servidor.send(nik)
    truck=servidor.recv('1')

servidor.close()    
