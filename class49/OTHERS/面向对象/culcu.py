class calcu():
    try:
        a=eval(input("a:"))
        b=eval(input("b:"))
    except NameError as e:
        b=eval(input("输入数据类型错误，请重新输入："))
    else:
        print("没有发生错误")
    def pluse(self):
         print(self.a+self.b)
    def miner(self):
        c=self.a-self.b
        print(c)
    def multi(self):
        c=self.a*self.b
        print(c)
    def devide(self):
        c=self.a/self.b
        print(c)

def calculator():
    op=calcu()
    s=input("请输入运算符：")
    if s=="+":
        op.pluse()
    if s=="-":
        op.miner()
    elif s=="*":
        op.multi()
    elif s=="/":
        op.devide()
calculator()



