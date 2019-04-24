import socket

#获取对象
s=socket.socket()
#连接服务器;地址通过ip和端口号识别
#不能跟本机端口号重叠，往大了取5000-8000
s.connect(("192.168.7.200",5000))
#3.发送消息:需要发送字节流,encode()默认转gbk格式
#消息相关方send();recv()
while True:
    send_msg=input("your massage:")
    s.send(send_msg.encode())
    msg=s.recv(1024).decode()
    print(msg)

























# import socket
# s=socket.socket
# s.connect(("192.168.7.200",554))
# s.send("hello zyf".encode())