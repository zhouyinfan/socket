# 1.编写三个类：person（eat()，sleep()）、teacher（teach()）、
# student(listen())，teacher和student需继承于person，student需重写person中的eat方法。
class person:
    def eat(self):
        print("eating......")
    def sleep(self):
        print("sleeping......")
class teacher(person):
    def teach(self):
        print("teaching......")
class student(person):
    def listen(self):
        print("listenin......")
    def eat(self):
        print("finished eating..........")
# p=person()
# t=teacher()
# s=student()
# p.eat()
# s.eat()
# t.sleep()

# 2.在上面的例子中另外再创建一个类class_room, class_room中有成员teacher和student对象，还有teach方法(重写)。
class person:
    def eat(self):
        print("eating......")
    def sleep(self):
        print("sleeping......")
class teacher(person):
    def teach(self):
        print("teaching......")
class student(person):
    def listen(self):
        print("listenin......")
    def eat(self):
        print("finished eating..........")
class class_room(teacher,student):
    def teach(self):
        print("she is no teacher anymore......")
# cr=class_room()
# cr.teach()



# 3.写成了一个游戏机器人自动游戏比赛，说明：先定义一个基类：
# AutoPeople，类中存在一个全局类成员，所有队员有效
# GameDic = ['石头','剪刀','布']含义为 石头>剪刀>布>石头 等
# 然后需要定义一个分数值 Score，完成两个机器人之间的比赛！

import random
class AutoPeople(object):
    GameDic= ['石头','剪刀','布']
    Score=0
    def choose(self):
        result=random.choice(self.GameDic)
        return result
def Game():
    AP1 = AutoPeople()
    AP2 = AutoPeople()
    while True:
        AP=AP1.choose()
        PA=AP2.choose()
        print("AP1: AP2=%s:%s" %(AP,PA))
        if  (AP=="石头" and PA=="布") or (AP=="剪刀" and PA=="石头") or(AP=="布" and PA=="剪刀"):
            AP1.Score+=1
        elif AP!=PA:
            AP2.Score+=1
        if(AP1.Score==3 or AP2.Score==3):
            if AP1.Score>AP2.Score:
                print("AP1胜利")
                break
            else:
                print("AP2胜利")
                break

    print(AP1.Score)
    print(AP2.Score)
Game()


# 4.有一对兔子从出生后3月起一个月生一对小兔子，小兔子长到
# 第三个月后每个月又生一对兔子，假如兔子都不死，问每个月
# 的兔子总数是多少对？

class Rabbit:
    month=1
    def group(self):
        self.month+=1
    def birth(self,rabit_list):
        rabit_list.append(Rabbit())

def judge(n):
    rabit_list=[Rabbit()]
    for j in range(n):
        for i in rabit_list:
            if i.month<3:
                i.group()
            else:
                i.birth(rabit_list)
    print(len(rabit_list))
# judge(12)





