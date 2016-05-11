#多级菜单
# 思路：
# 1，创建一个三级字典，一级字典包含各省，二级字典里包含各市，第三级列表里包含各区
# 2，运行程序，先把一级字典里的key显示并把索引也显示提供选择
# 3，如果选择一个索引，下一步把索引对应的二级字典里的key也显示出来，以此类推
# 4，用户输入“q”就退出整个程序，输入“b”就返回到上一级字典
city = {
    "北京":{
        "昌平区":["天通苑""回龙观","沙河"],
        "朝阳区":["CCTV","建外SOHO"],
    },
    "河南":{
        "郑州":["金水区","二七区","东城区"],
        "周口":["郸城县","沈丘县","沙河"],
    },
}

flag=False										#定义flag一个标志位，就是为了退出整个循环
while not flag:                                 #定义flag为假,取反为真开始循环；
    for i,k in enumerate(city.keys()):          #把第一层字典的key和索引号都显示出来；
        print(i,k)
    print("-->")
    name1 = input("input your num:").strip()
    if name1 == "q":                            #如果输入“q” ，flag就为真，取反为假下面就不在执行直接退出程序；
        flag=True
    elif name1.isdigit():						#判断输入参数是否为数字
        name1=int(name1)                        #如果输入的是数字，把字符数字转换成数字格式
        key1=list(city.keys())[name1]           #因为字典没有索引值，需转换成列表，取出索引值对应的元素
        while not flag:
            for i1,k1 in enumerate(city[key1]):     #遍历第二级字典的key，并显示索引
                print(i1,k1)
            print("-->-->")
            name2 = input("input your num:").strip()
            if name2 == "b":                    #如果输入“b”，返回上一级
                break
            elif name2 == "q":                   #如果输入“q” ，flag就为真，循环将不再执行直接退出程序；
                flag = True
            elif name2.isdigit():
                name2=int(name2)
                key2=list(city[key1].keys())[name2]  #取出第三级索引值对应的元素，
                while not flag:
                    for i2,k2 in enumerate(city[key1][key2]):   #列出第三级字典的key，并显示索引
                        print(i2,k2)
                    print("-->-->-->")
                    name3 = input("input your num:").strip()
                    if name3.isdigit():
                        print("Sorry, this's last layer")
                    elif name3 == "b":
                        break
                    elif name3 == "q":
                        flag=True



