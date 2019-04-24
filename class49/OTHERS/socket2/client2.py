import socket
import time
class Client():
    def __init__(self):
        self.s=socket.socket()
        self.s.connect(("192.168.7.200",5999))
    def send_recv(self):
        nickname= input("你的昵称:")
        while True:
            send_msg = input("请输入信息:")
            t1 = time.strftime('%H:%M:%S')
            self.s.send((nickname + ' '+ t1 + ' '+':'+' '+ send_msg).encode())
            if send_msg=="exit":
                exit("客户端已下线。。")
            msg=self.s.recv(1024).decode()
            print(msg)
if __name__ == '__main__':
    client=Client()
    client.send_recv()
    # 3.
    # 实现一个客户端可以重复向服务端发送消息；
    # 同时当客户端输入exit时，客户端下线，服务端正常关闭。


