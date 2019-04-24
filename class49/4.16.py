# lis1=[1,2,34,56,7,2,4,2]
# print(id(lis1))
# lis2=[3,4,[5,6]]
# lis3=lis1+lis2
# print(lis3)
# lis4=lis3[1:3:1]
# print(lis4)
# for i in lis3:
#     print(i)
#内置函数
##增
#append 整体加进去
# lis1.append([1,2,3,4])
# print(lis1)
# print(id(lis1))
#extend将元素拆分开加进去，可迭代对象
# lis1.extend([1,2,3])
#中间加元素
# lis1.insert(2,"hello")
# print(lis1)
##删
# del lis1[0]
#print(lis1)--关键字，del下标或者列表名
# lis1.pop(1)
# print(lis1)
# lis1.remove(2)
# print(lis1)
#remove 要删除特定的值，可以通过循环来删
# for i in lis1:
#     if i==2:
#         lis1.remove(i)
# print(lis1)
#-------------------练习分割线
# 1.创建一个列表，内部嵌套了3个列表
# a=['xiaoming','student',10],
# b=['xiaohong','coder',23],
# c=['xiaohuang','boss',35]，
# 打印第2个列表的第1个元素，打印第3个列表的所有数据，
# 删除第2个列表，打印整个大列表数据。
# lis=[['xioaming','student',10],['xiaohong','coder',23],['xiaohuang','boss',35]]
# print(lis[1][0])
# print(lis[2])
# lis.remove(2)
# print(lis)
##查
#查找元素下标，找到返回下标，默认匹配第一个元素

# print(list1.index(3))
# 统计元素个数
# print(list1.count(3))
#改
# list1[0]=9
# print(list1)
# list1.reverse()
# print(list1)
# list1.sort()
# print(list1)
# list1.reverse()
# print(list1)
# list1.sort(reverse=True)
# print(list1)
# 2.将第1题中的大列表的末尾添加一个元素10。
# lis=[['xioaming','student',10],['xiaohong','coder',23],['xiaohuang','boss',35]]
# a) 将添加的元素通过列表打印出来。
# lis.append(10)
# print(lis)
# b）输出大列表中出现10这个元素的次数。
# count=0
# num=0
# for i in lis:
#     if i==10:
#         count+=1
#     else:
#         num+=i.count(10)
# print(count+num)




# print(lis.count(10))
# c）输出第1个子列表中出现第一个元素‘10’的位置。
# print(lis[1].index(10))
# d）对此列表进行反序输出。
# lis.reverse()
# print(lis)
# e）移除第2个子列表中的第3个元素，输出整个列表。
# del(lis[1][2])
# print(lis)
# list[1].pop(2)
# print(lis)
# f）移除整个列表中所有出现‘10’的元素并输出。

# 3. 在歌星大奖赛中，有10个评委为参赛的选手打分，分数为1~100分。
# 选手最后得 分为：去掉一个最高分和一个最低分后其余8个分数的平均值。请编写一个程序实现。
# sl=[]
# for i in range(0,10):
#     score=eval(input("输入分数"))
#     sl.append(score)
# print(sl)
# sl.sort()
# sl.pop(0)
# sl.pop()
# sum=0
# for i in sl:
#     sum+=i
# print(sum/8)
#sl=[]
# for i in range(0,10):
#     score=eval(input("请输入一个分数"))
# tup=("a",12,43,65,12)
# print(type(tup))
# print(tup[3])
# tup1=(6,)
# tup2=tup+tup1
# print(tup2)
# print(tup[1:4])
# for i in tup:
#     print(i)
# print(tup.index(12))
# print(tup.count(12))
# print(tup)
# print(len(tup))
# 1.创建一个元组，分别进行索引、添加、长度计算、切片操作。
# yuanzu=("z","y","f",1,2,3)
# print(yuanzu.index("f"))
#
# print(len(yuanzu))
# yuanzu2=yuanzu[0:3]
# print(yuanzu2)

# 2.创建两个元组，进行连接操作。
# yuanzu3=yuanzu+yuanzu2
# print(yuanzu3)
# 3.创建一个列表和元组，将其连接后打印出
# 集合
# set1={2,3,4}
# set2={2,3,5}
#交集set3=set1&set2
#并集set3=set1|set2
#差集set3=set1-set2
#差集set3=set2-set1
#表示set2与set1不一样的元素
# set2.add(6)
# print(set2)
# set1.update(set2)
# print(set1)
# 1.使用花括号和set创建各一个集合。
# 2.对第1题中的集合进行交、并、差集运算。
# dic={"k1":1,"k2":[1,2,3],"k3":10,"k4":"hello"}
# for i in dic:
#      if dic[i]==10:
#          print(i)
#dic["k2"]="hello"
# dic2={1:"a",2:"b"}
# dic.update(dic2)
# dic1=dic.fromkeys([3,4],"hello")
# print(dic1)
# a=dic.setdefault(2,"hello")
# b=dic.setdefault(3,"hello")
# a=dic.get("k2")
# print(a)
# del dic["k1"]
# dic.pop(2)
# dic.clear()
# print(dic)
# a=dic.keys()
# a=list(a)
# print(a[0])
# a=dic.values()
# print(a)
# a=list(a)
# print(a[0])
#1. 创建一个字典dic1,并练习增删查改的操作。
# dic1={"k1":1,"k2":2,"k3":3,"k4":4}
#增
# dic1["k5"]=5
# print(dic1)
# dic2={"k6":6,"k7":7}
# dic1.update(dic2)
# print(dic1)
# dic1.setdefault("k8",8)
# print(dic1)
# dic2=dic1.fromkeys([1,2,3,4,5,6],"hello")
# print(dic2)
#查找
#dic1={"k1":1,"k2":2,"k3":3,"k4":4}
# a=dic1.setdefault("k1",2)
# print(a)
# print(dic1["k2"])
# print(dic1.get("k3"))
#改
# dic1["k2"]=5
# print(dic1)
#删
# dic2={"k1":1,"k2":2,"k3":3,"k4":4}
# del dic2
# print(dic2)
#其他操作
# dic1={"k1":1,"k2":2,"k3":3,"k4":4}
# a=dic1.keys()
# print(a)
# a=list(a)
# b=a[1]
# print(b)
# b=dic1.values()
# print(b)
# b=list(b)
# c=b[2]
# print(c)
#  2.创建一个列表，里面的有两个元素，每个元素是一个字典：
# dic1 = {'name':'zhangsan','age':'20'}
# dic2 = {'name':'lisi','age':'22'}
# 1）对此列表中的第2个元素（字典）中的age修改为23。
# lis1 = [{'name':'zhangsan','age':'20'},{'name':'lisi','age':'22'}]
# a=lis1[1]
# a['age']=23
# print(lis1)
# 2）向此列表再添加一个元素,仍然为字典dict3 = {'name':'wang','age':'30'}。
# dict3 = {'name':'wang','age':'30'}
# lis1.append(dict3)
# print(lis1)
# 3）打印列表中第一个元素的所有键。
# c=lis1[1]
# d=c.keys()
# print(d)
# 要求：以上不能直接操作dic，而是操作列表。
# 3.给定一个成绩单（字典），找出最大最小值，并求出平均成绩。成绩自己定义！
#最重要的就是要讲字典转化为元组
# sc={"a":89,"b":67,"c":54,"d":33}
# score=sc.values()
# score=set(score)
# score1=max(score)
# score2=min(score)
# avg=sum(score)/len(score)
# print(score1)
# print(score2)
# print(avg)
# 4.已知列表score =[45,98,65,87,43,83,68,74,20,75,85,67,79,99] ，
# 统计并以字典的形式输出各成绩等级的人数。
# 等级A:（90~100）B:(80~89) C:(70~79) D:(60~69) E:(60以下)
# score =[45,98,65,87,43,83,68,74,20,75,85,67,79,99]
# dic1={}
# a = 0
# b = 0
# c = 0
# d = 0
# e = 0
# for i in score:
#     if i>=90 and i<=100:
#         a+=1
#     elif i>=80 and i<=89:
#         b+=1
#     elif i>=70 and i<=79:
#         c+=1
#     elif i>=60 and i<=69:
#         d+=1
#     else:
#         e+=1
# dic1["A级"]=a
# dic1["B级"]=b
# dic1["C级"]=c
# dic1["D级"]=d
# dic1["E级"]=e
# print(dic1)
# A=0
# B=0
# C=0
# D=0
# E=0
# score =[45,98,65,87,43,83,68,74,20,75,85,67,79,99]
# for i in score:
#     if i<101 and i>=90:
#         A+=1
#     elif i>=80 and i<=89:
#         B+=1
#     elif i>=70 and i<=79:
#         C+=1
#     elif i>=60 and i<=69:
#         D+=1
#     else:
#         E+=1
# dic4={}
# dic4['A:']=A
# dic4['B:']=B
# dic4['C:']=C
# dic4['D:']=D
# dic4['E:']=E
# print(dic4)
# 5.分别输入年、月、日，判断此日期是当年的第几天。
# （把闰年考虑进去,能被4整除且不能被100整除或者能被400整除的为闰年）
year=eval(input("今年是哪一年："))
month=eval(input("现在几月："))
day=eval(input("今天是该月第几天："))
if (year%4==0 and year%100!=0)or year%400==0:
    dic1={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    num=0
    for i in range(month+1):
        if i in dic1.keys():
            num+=dic1[i]
day=day+num
print("现在是今年第%d天"%(day))
