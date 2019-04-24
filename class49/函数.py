 #定义一个计算器函数，输入a,b和运算符+-*/
def pluse(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def multi(a,b):
    print(a*b)
def divi(a,b):
    print(a/b)
def calcu(a,b,c):
    if c=="+":
        pluse(a,b)
    elif c=="-":
        sub(a,b)
    elif c=="*":
        multi(a,b)
    elif c=="/":
        divi(a,b)
#calcu(1,2,"-")
def calcu(a,b,c):
    if c=="+":
        print(a+b)
    elif c=="-":
        print(a-b)
    elif c=="*":
        print(a*b)
    elif c=="/":
        print(a/b)
#calcu(1,2,"/")
#4.17晚自习作业
'''1. （完成）定义一个函数，实现一个班级（10 个学生，名字自定）随机点名的功能'''
import random
def call_stu():
    lis1=["张三","李四","王二","麻子","周一","巫九","郑琦","赵四","钱八","孙子"]
    i=random.choice(lis1)
    print(i)
#call_stu()
'''2.(完成) 输入4个整数x,y,z,m，请把这四个数由小到大输出。（禁止使用列表的 sort方法）'''
def order_s_m():
    x=eval(input("输入数："))
    y=eval(input("输入数："))
    z=eval(input("输入数："))
    m=eval(input("输入数："))
    global lis
    lis=[x,y,z,m]
    len1=len(lis)
    for i in range(0,len1-1):
        for j in range(0,len1-i-1):
            if lis[j]>lis[j+1]:
                lis[j],lis[j+1]=lis[j+1],lis[j]
#order_s_m()
#print(lis)
'''3.（完成） 有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？'''
def new_num():
    global num
    num=0
    for x in range(1,5):
        for y in range(1,5):
            for z in range(1,5):
                if(x!=y)and(y!=z)and(x!=z):
                    print("%d%d%d"%(x,y,z))
                    num+=1
#new_num()
#print("可以组成%d个三位数"%num)
'''4. （完成）实现一个函数count(str,substr),查找str中有多少个substr，并返回个数。'''
def count(str,substr):
    global num4
    num4=0
    lis4=str.split(substr)
    num4=len(lis4)-1
#count("hkjsdjdjsjsasafkjdsaja","ja")
#print(num4)
def count1(str1,substr1):
    global count4
    len4=len(str1)
    len5=len(substr1)
    count4=0
    for i in range(0,len4-len5+1):
        if str1[i:i+len5]==substr1:
            count4+=1
    return count4
count1("lovelovelovelovinglove","love")
#print(count4)



'''（完成）5.定义两个列表，用于存放一批用户名和密码（按下标位置一一对应）
，用户同时输入用户名和密码，验证用户名和密码是否正确。
（3次之后不允许再登录。）'''
lis5=["z","y","f"]
lis6=["123","456","789"]
def log_in():
    usn=input("请输入用户名：")
    if usn in lis5:
        for i in range(0,3):
            pw=input("密码：")
            index=lis5.index(usn)
            if pw==lis6[index]:
                print("登陆成功")
                break
            else:
                print("密码错误")
    else:
        print("用户名不正确")
#log_in()
lis5=["z","y","f"]
lis6=["123","456","789"]
def log_in():
    pass
'''(完成) 继第5题，实现登录失败3次不允许再登录。（用户名和密码分开限制，各允许输入3次）'''
lis51=["z","y","f"]
lis61=["123","456","789"]
def log_in1():
    bl=True
    for j in range(0,3):
        if bl:
            usn=input("请输入用户名：")
            if usn in lis51:
                for i in range(0,3):
                    pw=input("密码：")
                    index=lis51.index(usn)
                    if pw==lis61[index]:
                        print("登陆成功")
                        bl=False
                        break
                    else:
                        print("密码错误")
            else:
                print("用户名不正确")
#log_in1()
'''6. (完成)数字处理：用户输入一个正整数，将该正整数倒序输出，并求各位数相加之和。
【要求不允许把用户输入的正整数，处理为字符串，只能按照数值运算的规律完成本题。】'''
def rever_pluse():
    num6=eval(input("请输入一个正整数："))
    global newn ,sumi
    newn=""
    sumi=0
    while num6>0:
        i=num6%10
        j=num6//10
        num6=j
        sumi+=i
        i=str(i)
        newn=newn+i
#rever_pluse()
#print(newn,sumi)
'''【扩展 1】继6题后，可进一步求小数的每一位之和，如 1234.567，并让该小数顺序按位输出'''

'''【扩展3】字符串判断：从键盘输入一个字符串，判断该字符串是否可以被转换为一个有效的数字。
(禁止使用 Python 自带方法完成)'''
def conv_str():
    str9=input("请输入一个字符串：")
    lis9=[]
    if str9.isdigit():
        print("该字符串可以转化为数字")
    else:
        print("该字符串不能转化为数字")
#conv_str()



