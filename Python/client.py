import socket
encoding = 'utf-8'
HOST = 'localhost'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print('[CLIENTE]Para sair use CTRL+X\n')

msg = input('[CLIENTE]Digite algo: ')
while msg != '\x18':
    tcp.send(bytes(msg,encoding))
    data = tcp.recv(1024)
    print('from SERVER:', data)
    msg = input('[CLIENTE] Digite algo: ')
tcp.close()