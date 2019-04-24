import socket
import time
class Server:
    def __init__(self):
        self.s = socket.socket()
        self.s.bind(("192.168.7.200", 5999))
        self.s.listen(5)
        self.con, addr = self.s.accept()
        # print(con)
        # print(addr)
    def recv_send(self):
        # nickname = self.con.recv(1024).decode()
        # self.con.send((nickname).encode())
        while True:
            msg = self.con.recv(1024).decode()
            new_msg=msg.split(" : ")
            if new_msg=="exit":
                exit("服务器已下线。。。")
            else:
                print(msg)
                self.con.send(msg.encode())
if __name__ == '__main__':
    server=Server()
    server.recv_send()

    # 4.实现给一个客户端取昵称，该客户端向服务端发送消息，
    # 服务端返回该客户端的消息【消息格式：“昵称 16:01:40 ：xxxx”】
