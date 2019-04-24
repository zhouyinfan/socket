import socket
class Client:
    def __init__(self):
        self.s=socket.socket()
        self.s.connect(("192.168.7.200",6000))
    def send_recv(self):
        while True:
            send_msg = input("your massage:")
            self.s.send(send_msg.encode())
            msg=self.s.recv(1024).decode()
            print(msg)
if __name__ == '__main__':
    client=Client()
    client.send_recv()
    # 3.
    # 实现一个客户端可以重复向服务端发送消息；
    # 同时当客户端输入exit时，客户端下线，服务端正常关闭。

# 4.实现给一个客户端取昵称，该客户端向服务端发送消息，
# 服务端返回该客户端的消息【消息格式：“昵称 16:01:40 ：xxxx”】




