def start_menu():
    tip = '''
***************** 欢迎来到WoniuATM **********************
***************** 请选择操作菜单 ************************
************* 1. 注册   2. 登录   3. 退卡 ***************
    '''
    print(tip)
    option = input("请输入你的操作选项：")
    if option == "1":
        register()
    elif option == "2":
        login()
    else:
        exit('谢谢，欢迎下次光临.')

def main_menu():
    tip = '''
*************************** 恭喜登录蜗牛银行 **********************************
*************************** 请选择操作菜单 ************************************
************ 1. 查询   2. 取款   3. 存款   4. 转账   5. 退卡 ******************
        '''
    print(tip)
    option = input("请输入你的操作选项：")
    if option == "1":
        balance_quiry()
    elif option == "2":
       withdraw()
    elif option == "3":
        deposit()
    elif option == "4":
       pass
    elif option == "5":
        exit('谢谢，欢迎下次光临.')

'''登录选项...........................................................'''
def f_r_w():
    file=open(r"C:\Users\Administrator.USER-20190305CL\Desktop\lis.txt")
    content=file.read()
    lis=content.split("\n")
    file.close()
    print(lis)
    dic1={}
    for i in lis:
        lis2=i.split(",")
        dic1[lis2[0]]=lis2[1]
        return dic1
f_r_w()
# def login():
#     global user
#     for i in range(3):
#         user=input("请输入用户名：")
#         pw=eval(input("请输入密码："))
#             if user in lis:
#                 index=lis.index(user)
#                 if pw==lis[index+1]:
#                     print("登陆成功")
#                     break
#                 else:
#                     print("密码错误")
#             else:
#                 print("用户名错误")
#         else :
#             print("您已输入超过三次")
# login()
'''注册...........................................'''
def register():
    for i in range(0,3):
        user=input("请输入用户名：")
        if user not in dic1:
            pw=input("请输入密码：")
            print("注册成功")
            dic1[user]=pw
            print(dic1)
            start_menu()
        else:
            print("改用户名已被注册")
    else:
        print("您已输入超过三次")
        start_menu()

#register()
'''余额查询'''
dic_balan={"jack":100,"rose":2000,"mary":333}
def balance_quiry():
    print("你的余额为%d元"%dic_balan[user])

'''取款'''
def withdraw():
    global balance
    amount=eval(input("请输入你的取款金额："))
    if amount<dic_balan[user]:
        balance=dic_balan[user]-amount
        print("你的余额为%d"%balance)
#start_menu()
'''存款'''
def deposit():
    amount=eval("请输入你要存入的金额：")
    new_balance=balance+amount
    print("你的余额为：%d"%new_balance)

    '''文件读写。。。。。'''
