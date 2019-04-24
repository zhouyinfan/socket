import socket
class Server:
    def __init__(self):
        s = socket.socket()
        s.bind(("192.168.7.200", 6000))
        s.listen(5)
        self.con, addr = s.accept()
        # print(con)
        # print(addr)
    def recv_send(self):
        while True:
            msg = self.con.recv(1024).decode()
            print(msg)
            ser_mag = input("请输入信息：")
            self.con.send(ser_mag.encode())
if __name__ == '__main__':
    server=Server()
    server.recv_send()
