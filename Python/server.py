import socket
HOST = 'localhost'              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print (('[SERVIDOR]Conectado por'), cliente)
    while True:
        msg = con.recv(1024)
        if not msg: break
        orga = sorted(msg)
        con.send(bytes(orga))
        print('[from CLIENTE]: ', cliente, msg)
    print (('[SERVIDOR]Finalizando conexao do cliente'), cliente)
    con.close()