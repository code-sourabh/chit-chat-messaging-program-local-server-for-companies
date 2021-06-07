def client():
    client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    client.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)
    ip_client = "192.168.43.56"
    port_client = 1113
    client.connect(( ip_client,port_client ))
    while True:
        print("send ur msg")
        msg_client = input()
        client.sendall(msg_client.encode())
        if "bye" in msg_client.decode():
            break
    return print("connection closed now !!!! ")

def server():
    server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)
    ip_server = "192.168.43.221"
    port_server = 1112
    server.bind((  ip_server , port_server ))
    while True:
        server.listen()
        server_object , addr_info_client = server.accept()
        msg_client = server_object.recv(1024)
        print(msg_client)
        if "bye" in msg_client.decode():
            break
    return print("connection closed")

client_thread = threading.Thread(target = client , name="t1" )
server_thread = threading.Thread(target = server , name= "t2")

client_thread.start()
server_thread.start()
