#实现一个服务端
import socket
#获取对象
s=socket.socket()
#2.绑定ip和端口号
s.bind(("192.168.7.200",5000))
#开启监听,5代表一次只能监听5个客户端对象：如果有多的客户端，排队等待
s.listen(5)
#等待接受客户端的连接;con代表链接上的客户端对象，addr代表客户端ip端口号
con,addr=s.accept()
print(con)
print(addr)
#接受和发送消息：send();recv()
#接收消息，一般缓冲区大小给1024吧，只接受不超过
while True:
    msg=con.recv(1024).decode()
    print(msg)
    ser_mag=input("请输入信息：")
    con.send(ser_mag.encode())