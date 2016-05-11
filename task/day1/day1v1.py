#!/usr/bin/env python
# -*- coding:utf-8 -*-

#用户登陆，
#输入用户名密码
#认证成功后显示欢迎
#输错三次锁定
#
#思路：
#一，先创建两个数据库，没有用文件代替，文件一（黑名单.txt）文件二（用户列表包括用户名和密码.txt）
#二，验证输入用户有没有在黑名单里面，有就退出
#三，如果用户名没有在黑名单里，就输入密码去读用户列表里面读取
#四，验证用户和密码是否对应，对退出，不对循环次数加一进入下一次循环
#五，连续输错三次把用户名追加到黑名单内

# f=open("heimingdan.txt","w")  #创建文件，注意第一次创建完文件之后，此代码需注释掉，f.write（）会把原来的文件覆盖掉
# f.write("xiaohei\n")
# f.write("lixiaolong\n")
# f.write("zhangjie\n")
# f.close()
#
# k=open("userlist.txt","w")
# k.write("xiaobai 888888\n")
# k.write("tianjie 123qwe\n")
# k.write("malimin 123456\n")
# k.close()

import sys #调用sys模块，
def show(user):    #定义一个函数，用于用户连续输错三次，加入黑名单
    print("%s 用户锁定" % (user))
    f = open("blacklist.txt", "a")
    f.write("\n" + user)

def black(user):    #定义一个函数，用于输入的用户如果在黑名单中就退出
    with open("blacklist.txt","r") as f: #打开blacklist.txt文件，用with..as.. 是为了防止最后忘了关闭文件
        for line in f.readlines():
            if line.strip() == user :      #遍历blacklist.txt这个名单是否有与用户输入的名字相等的
                sys.exit("用户'%s'已被锁定"%(user))   #如果相等直接退出程序

a=0                     #定义循环次数初始值
user_count=0            #定义用户锁定次数初始值
user_test=""           #定义用户初始值，用于判定用户输入的是否是统一用户名
flag=False              #设定一个标志位，为了最后退出整个循环
while a<3:              #a小于3开始执行以下操作
    user=input("Input Your Username:")       #输入一个用户名，定义成一个变量
    black(user)                                 #调用上面定义的black函数，并把‘user’这个变量付给实参
    if user_test == user:                       #判断如果用户初始值，等于用户输入的值，那么用户锁定次数+1
        user_count += 1
    else:                                   #如果用户初始值不等于用户输入的参数，锁定次数-1，
        user_test=user
        user_count -=1
    password=input("Input Your Password:")    #输入密码
    with open("userlist.txt","r") as k:         #遍历"userlist.txt"文件
        for line in k.readlines():
            username,passwd=line.strip().split()   #把用户和密码分割成两个变量 用split()
            if username==user and passwd==password:    #如果密码用户都等于用户输入的参数
                flag=True                             #就把flag为真，否则就为假，这个地方就是为了退出整个循环
                break                               #只是跳出for循环
            else:
                flag=False
        if flag==True:
            print("%s欢迎来到地狱" % (user))       #在for 循环的外面继续判断，如果flag为真，显示成功并退出
            break
        elif flag==False:
            print("臭屌丝输错了....")             #还为False的话 循环次数加1 继续，直到a>=3为止
            a+=1
else:
    if user_count == 1:  #锁定用户调用前面定义的锁定用户加的函数，需要注意的是，用户连续输入三次相同的参数，才加入黑名单
        show(user)


















