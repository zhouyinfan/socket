'''a=5
b=10
c=a+b
print(c)
import keyword
print(len(keyword.kwlist))
'''
'''
a=eval(input("Number:"))
b=10
c=a+b
print(b-a)
'''
'''
a=input("my name is:")
b=int(input("my age is:"))
c=input("his name is:")
d=int(input("his age is:"))
print("我的名字是：%s 年龄是：%d 他的名字是：%s 年龄是:%d"%(a,b,c,d))
'''
'''
str="hello world!"
str1=str[3:7]
str2=str[8:9]
str3=str1+str2
print(str3)
'''
'''
str="abcdefghi"
str1=str[2:3]
str2=str[8:9]
str3=str[6:7]
str4=str[4:5]
str5=str1+str2+str3+str4
print(str5)
'''
'''
str="abcdefghi"
str6=str[-1:-8:-2]
print(str6)
'''
'''
a="hello"
b="world"
print(a+"   "+b)
print(a,b,end="***")
print(a,b,sep="###")
'''
#a=5
#b=input("put num:")
#print(a*b)
#print("*"*20)
'''
print(" "*8+"*")
print(" "*6+"*"*3)
print(" "*4+"*"*5)
print(" "*2+"*"*7)
print("*"*9)
'''
#print(" "*8+"*"+'\n'+" "*6+"*"*3+'\n'+" "*4+"*"*5+'\n'+" "*2+"*"*7+'\n'+"*"*9)
#print(" "*8+"*"," "*6+"*"*3," "*4+"*"*5," "*2+"*"*7,"*"*9,sep="\n")
'''
str1="hello you"
print(str1[0])
print(str1[6])
sub_str=str1[3:7:1]
print(sub_str)
str2=str1[::-1]
print(str2)
'''
'''
str="hello world!"
str1=str[3:4]
str2=str[8:9]
str3=str[3:6:2]
str4=str[6:9:2]
print(str3+str4)
print(len(str))
'''
'''
st="abcdefghi"
 
st1=st[-1:-8:-2]
st2=st[-2:-9:-2]
st3=st[2:9:2]

print(st1)
print(st2)
print(st3)
'''
'''
str2="abbcdebfgbfhbf"
index=str2.find("j")
index1=str2.index("h")
count=str2.count("b")
print(count)
split=str2.split("b")
print(str2)
str3=str2.replace("bf","you",2)
print(str3)
'''
'''
str1="how are you"
print(str1.isalpha())
print(str1.isdigit())
print(str1.isalnum())
print(str1.isspace())
print(str1.isupper())
print(str1.islower())
str2=str1.upper()
str3=str2.lower()
str4=str1.title()
str5=str1.capitalize()
print(str5)
'''
#str1="abcde"
#print(str1[::-1])
#s="you are beautiful you are beautiful"
#print(s[8:21])
#print(s.count("beautiful"))
'''
str="adc kdn lad"
str1=str.split("d")
print(str1[2],str1[3])
'''

# str="NIHAOnihao111***"
# for i in str:
#     u=0
#     l=0
#     d=0
#     o=0
#     if i.isupper():
#         u+=1
#     elif i.islower():
#         l+=1
#     elif i.isdigit():
#         d+=1
#     else:
#         o+=1
#
# print(u)
# print(l)
# print(d)
# print(o)


# pin=input("请输入密码：")
# if len(pin)<8 or len(pin)>16:
#     print("密码错误")
#     else:
#         if pin.isdigit() or pin.isalpha():
#             print("密码输入错误")
#         else:
#             for i in pin:
#                 if i.isspace():
#                     print("密码输入错误")
#                 else:
#                     print("密码正确")

#print("hello\\n")
# lis=['hello',12,33,'world',True,[1,[2,3]]]
# lis1=['a','b','c']
# lis2=lis+lis1
# print(lis2)
# lis[2]=22
# print(lis)
# del lis[2]
# print(lis)
# lis1[2]=22
# print(lis1)
# print(lis[5][0])
# print(lis[5][1][0])

# print(lis[3])
# print(type(lis))
# lis1=['hello','world']
# lis1.append('nihao')
# print(lis1)
# lis1.extend('haha')
# print(lis1)
# print(lis1.count('h'))
# print(lis1.index('h'))
# lis1.insert(1,'love')
# print(lis1)
# print(lis1.pop(1))
# print(lis1)
# lis1.remove("hello")
# print(lis1)
# lis1.reverse()
# print(lis1)
# print(lis1[::-1])
# lis1.sort()
# lis1=[21,43,532,65,2,5,53]
# lis1.sort(reverse=True)
# print(lis1)
#lis1=[['xiaoming','student',10],['xiaohong','coder',23],['xiaohua','boss',35]]
# print(lis1[1][0])
# print(lis1[2])
# lis1.pop(1)
# print(lis1)
# lis1.add("10")
# print(lis1)
# passwd=input("输入密码：")
# a=0
# num=0
# alp=0
# otc=0
# if len(passwd)>=8 and len(passwd)<=16:
#     for i in passwd:
#         if i.isspace():
#             a+=1
#            print("密码错误")
#            break
#         elif i.isdigit():
#             num+=1
#         elif i.isalpha():
#             alp+=1
#         else:
#             otc+=1
#     if a==0 and (num+alp+otc)>=2：
#         print("密码或输入成功！")
#     else:
#         print("密码错误")
# else:
#     print("长度不够")







