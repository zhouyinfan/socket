# -- 5.	数据库woniu里面有表格user_info，
# -- 检测A和B账户是否可用-检测账户A是否有100块-账户A减去100快，
# -- 账户B加上100块
# import pymysql
# class account:
#     def check(self,sql):
#         db = pymysql.connect("localhost", "root", "123456", "woniu_atm", charset="utf8")
#         cur = db.cursor()
#         cur.execute(sql)
#         result = cur.fetchall()
#         result1=result[0][0]
#         print(result1)
#         cur.close()
#         db.close()
#
#     def transfer(self,sql):
#         db = pymysql.connect("localhost", "root", "123456", "woniu_atm", charset="utf8")
#         cur = db.cursor()
#         cur.execute(sql)
#         cur.close()
#         db.close()
# a=account()
# a.transfer("update user_info set balance=balance-100 where user='daisy'")
# a.check("select balance from user_info where user='daisy'")
#
# def op_account(sql,user):
#     a1=eval(a.check(sql))
#     if a1>100:
#         name1=input("请输入你要转账的对象：")
#         a.transfer(sql)
#     else:
#         print("您的余额不足100，抱歉")

# 8.	用Python编程，假设一年期定期利率为3.25%，计算一下需要过多少年，一万元的一年定期存款连本带息能翻番
# 第一年：10000+10000*3.25%
# 的二年：10000+10000*3.25%+（10000+10000*3.25%）*3.25%
# num=10000
# n=0
# while True:
#     num=num+(num*0.0325)
#     n+=1
#     if num>=20000:
#         break
# print("%d年"%n)

# a="hello world"
# # a1=a.split()
# # print(a1)
# a2=a.split("")
# print(a2)
# 10.	一个不知道长度的字典，现在要把里面的键和值分别取出来，
# 拼装成 “键”+空格+“值”的形式，该怎么操作（手写代码）
# def get_ele():
# #     dic10={"k1":"nihao","k2":"hello","k3":"bonjour"}
# #     for i in dic10:
# #         print(i+" "+dic10[i])
# # get_ele()
# list=[1,2,3,4,5,2,1]
# list1=set(list)
# list2=list(list1)
# print(list2)
# set1={32,4,2,45,6}
# list1=list(set1)
# print(list1)
# 12.	读取D盘下demo1.txt里面的第二行内容并输出。
# def read_content():
#     file=open(r"D:/demo1.txt",mode="a+")
#     file.seek(0)
#     content=file.readlines()
#     print(content[1])
#     file.close()
# read_content()
import keyword
print(keyword.kwlist)