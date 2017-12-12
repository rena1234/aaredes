import socket

"""
    retorna
    1 para escolha 1, 2 para escolha 2, 0 para empate

    matriz_comp
    pedra 0
    papel 1
    tesoura 2
    
    0 = empate
    1 = 1 vencedor
    2 = 2 vencedor

    1 linha
    2 coluna
"""
def retorna_vencedor(escolha1, escolha2):
    matriz_comp = [[0, 2, 1],[2,0,1],[1,2,0]]
    return matriz_comp[escolha1][escolha2]

def retorna_num_escolha(escolha):
    if escolha.decode("utf-8") == 'pedra':
        return 0
    if escolha.decode("utf-8") == 'papel':
        return 1

    if escolha.decode("utf-8") == 'tesoura':
        return 2
    else:
        print("palavra errada")

udp_ip = '127.0.0.1'
udp_port = 8014
fd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
fd.bind((udp_ip,udp_port))

while True:
    r = fd.recvfrom(1000)
    escolha_cli_1 = r[0]
    endereco_cli_1 = r[1]
    num_escolha1 = retorna_num_escolha(escolha_cli_1) 

    r = fd.recvfrom(1000)
    escolha_cli_2 = r[0]
    endereco_cli_2 = r[1]
    num_escolha2 = retorna_num_escolha(escolha_cli_2)

    if retorna_vencedor(num_escolha1, num_escolha2) == 0:
        fd.sendto(bytearray("empate","utf-8"), endereco_cli_1)
        fd.sendto(bytearray("empate","utf-8"), endereco_cli_2)

    if retorna_vencedor(num_escolha1, num_escolha2) == 1:
        fd.sendto(bytearray("ganhou","utf-8"), endereco_cli_1)
        fd.sendto(bytearray("perdeu","utf-8"), endereco_cli_2)

    if retorna_vencedor(num_escolha1, num_escolha2) == 2:
        fd.sendto(bytearray("perdeu","utf-8"), endereco_cli_1)
        fd.sendto(bytearray("ganhou","utf-8"), endereco_cli_2)
