# print("hello world!") #字符串
# print(2333) #整数
# print(2.333) #小数
# print(True,False) #布尔值
# print(None) #空,null
# print(()) #元组
# print([]) #数组/列表
# print({}) #字典

# print(1,end="&")#end是相邻print之间不换行，而是以end=""引号内的内容为连接，可以是有内容的比如一个符号，也可以是空白
# print(2,end="&")
# print(3,end="")

# print("哈哈"+"嘻嘻")#字符串相加是拼接的效果

# print("哈哈"*10)#字符串乘以多少就是显示多少个相同的字符串

# print(1+1)
# print(0.1+0.2)
# print(1+0.1)#整数和小数都可以实现正常的数学运算

# print(10//3)#取整
# print(10%3)#求余

# print(1==2 or 1 < 3)#判断为true

# a = 1  #把1这个值赋值给a这个变量，变量名要取得有意义，且小写字母开头
# print(a)

# name = "零" #把零这个值赋给name这个变量
# print(name)

# b = input("请输入:")
# print("input获取到的值:",b)

# c = input("请输入第一个数字:")
# d = input("请输入第二个数字:")
# print("和:",c+d)




# x = type("hahaha")#type获取数据类型
# print(x)

# e = str(2333)
# print(type(e))#把2333转换成str类型
"""
1、任何数据格式都可以转换为字符串
2、字符串要转换成其他类型，需要满足“长得像”这个条件
"""
# a = input("请输入第一个数")
# b = input("请输入第二个数")
# print("和：",float(a)+float(b))

# c = float(input("请输入第一个数字:"))
# d = float(input("请输入第二个数字:"))
# print("和:",c+d)

# name = input("请输入你的姓名:")
# age = input("请输入你的年龄:")
# habit = input("请输入你的爱好:")
# print("大家好,我叫{},我今年{}岁,我的爱好是{}。".format(name,age,habit))

#内容比较多的时候怎么写：
# print("大家好,我叫{mingzi},我今年{nianling}岁,我的爱好是{aihao},我叫{mingzi},我今年{nianling}岁,我的爱好是{aihao}。".format(mingzi=name,nianling=age,aihao=habit))

# print(1>2)

# print(len(a))

# a = len("哈哈哈哈哈哈哈哈哈")
# print(a)

"""
请实现一个计算输入的内容的长度是单数还是双数
"""
# print("0:代表偶数;1:代表奇数")
# lstr = input("请输入您要计算的内容：")
# print(len(lstr)%2)



# my_yuanzu = (1,2,3,"哈哈","嘻嘻",True,None) #元组
# print(my_yuanzu)#元组可以让我们少写几个变量；每个变量都会占用计算机的内存，变量越多，占的内存越多
# #下标就是计算机自动给我们的值编的号，是从0开始 
# #下标 从左往右数 0 1 2 3 4  从右往左数 -1 -2 -3 -4
# print(my_yuanzu[3])
# print(my_yuanzu.index("哈哈"))#获取“哈哈”这个值的下标
# print(my_yuanzu.count(1))#获取“1”这个值的个数，True也是1

# a = (1,2,3,9,8)
# b = (4,5,6,a)
# print(b)#二维元组（多维元组，有多少层就是几维）
# print(b[-1][1])#输出b元组下标为-2的值（也就是a元组）中的下标为1的值
# #求二维元组里面值的下标  a[-1].index("值")
# print(a[0:3])#切片 左闭右开  取元组中的第几个值到第几个值


# my_liebiao = [1,2,3,4,5,6] #列表
# print(my_liebiao)

# b = ("hi","hello")
# a = [1,2,3,4,5,6,"哈哈","嘻嘻",True,False,None,b]
# print(a)

# name = input("请输入您的名字：")
# a.append(name)
# a.insert(0,name)#0代表插入位置的下标
# xx = a.pop(7)#把下标为6的值取出来 赋值给xx变量
# print(xx)
# c = ["今天","明天","后天"]
# a.extend(c)#extend可以插入多个值 append只能插入一个值
# print(a)

# d = [2,1,4,5,3]
# d.sort()#正序
# d.sort(reverse=True)#倒序
# d.reverse()#颠倒
# d.clear()#清空d
# d.remove(5)#把d里面5这个值移除 注意remove括号里填的是值 不是下标（如果值有多个重复的 只删除一个）
# print(d)

"""
元组和数组的操作方式一模一样
区别是元组不可以修改，数组可修改（修改是指 比如往里面添加要素等操作）
"""

# my_zidian = {"username":"liuyun", "password":"a123456"} #字典：json格式 键key 值value
# print(my_zidian)
