# 6.用户输入一个字符串，如果字符串包含“h”,则输出“包含h......”；否则输出“不包含h”。10'
# str=input("请输入字符串：")
# if str.find("h")==-1:
#     print("不包含h...")
# else:
#     print("包含h....")
# 7.现有列表list1 = ["k",["qwe",20,{"k1":["tt",3,"1"]},89],"ab"]，其中的数字3变成字符串"100"(用两种方法)。10’
# list1 = ["k",["qwe",20,{"k1":["tt",3,"1"]},89],"ab"]
# list1[1][2]["k1"]=["tt","100","1"]
# list1[1][2]["k1"][1]="100"
# print(list1)
# 8.现有小明的成绩列表li1=[89,73,100];小红的成绩列表li2=[88,96,79];小黄的成绩列表li3=[60,82,91];
# （1）分别求三人的平均分，并将相应的分值以键值对的形式（人名：分值）添加到字典里存储起来。15'
# （2）求平均分最高的学生名字？
# li1=[89,73,100];li2=[88,96,79];li3=[60,82,91]
# avg1=sum(li1)/len(li1)
# avg2=sum(li2)/len(li2)
# avg3=sum(li3)/len(li3)
# dic1={}
# dic1["xiaoming"]=avg1
# dic1["xiaohong"]=avg2
# dic1["xiaohuang"]=avg3
# print(dic1)
# max_score=max(dic1.values())
# for i in dic1:
#     if dic1[i]==max_score:
#         print(i)
#1.顺序结构
#循环结构--循环做加法，求4~50之和
# num=0
# for i in range(4,50):
#     num=num+i
# print(num)
# passwd=input("输入密码：")
# a=0
# num=0
# alp=0
# otc=0
# if len(passwd)>=8 and len(passwd)<=16:
#     for i in passwd:
#         if i.isspace():
#             print("有空格，错误")
#             a=1
#             break
#         elif i.isdigit():
#             num=1
#         elif i.isalpha():
#             alp=1
#         else:
#             otc=1
#     if a==0 and (num+alp+otc)>=2:
#         print("密码或输入成功！")
#     else:
#         print("密码错误")
# else:
#     print("长度不对")
#密码长度8-16，不能包含空字符串，必须包含数字字母符号三种中的两种
# passwd=input("输入密码：")
# a=0
# num=0
# alp=0
# otc=0
# if len(passwd)>=8 and len(passwd)<=16:
#     for i in passwd:
#         if i.isspace():
#             print("有空格，错误")
#             a=1
#             break
#         elif i.isdigit():
#             num=1
#         elif i.isalpha():
#             alp=1
#         else:
#             otc=1
#     if a==0 and (num+alp+otc)>=2:
#         print("密码或输入成功！")
#     else:
#         print("密码错误")
# else:
#     print("长度不对")
# 1.输入两个数 a, b，如果a大于b且b>20则输出a+b，
# 如果a<b或a为负数则输出a-b，其他情况输出a*b。
def pr_ab():
    a=eval(input("input a:"))
    b=eval(input("input b:"))
    if a>b and b>20:
        print(a+b)
    elif a<b or a<0:
        print(a-b)
    else:
        print(a*b)
#pr_ab(2)

# 3.猜数字游戏：系统随机生成一个 1000 以内的正整数，用户输入一个数字，
# 如果输入数字大于系统数字则提示‘大了’，反之提示‘小了’，直到相等游戏结束，
# 提示‘通关并输出 猜测次数。（提示：可以 import random 来生成随机数）。

import random
def guess_num():
    b=0
    num=random.randint(0,1000)
    print(num)
    while True:
        a = eval(input("put num:"))
        b+=1
        if a>num:
            print("大了")
        elif a<num:
            print("小了")
        else:
            print("你猜对了,共猜了%d次"%(b))
            break
#guess_num()
#打印
#        *
#       **
#      ***
#     ****
#    *****
#  *******
def picture():
    for i in range(1,7):
        print(" "*(6-i)+"*"*i)
#picture()
file=open(r"C:\Users\Administrator.USER-20190305CL\Desktop\zyf.txt")
content=file.read()
print(content)
print(type(content))
file.close()