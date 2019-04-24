import  threading
import time
def movie():
    for i in range(3):
        print("watching movie")
        time.sleep(1)
def music():
    for i in range(3):
        print("listening to music")
        time.sleep(1)

#创建线程,target=函数名，代表指向的函数，args代表传参，元组形式
t1=threading.Thread(target=movie)
t2=threading.Thread(target=music)
#开启线程
t1.start()
t2.start()
#待子线程结束后再执行主线程
t1.join()
t2.join()
#主线程的代码
print("finished")