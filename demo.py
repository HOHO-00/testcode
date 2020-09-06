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




x = type("hahaha")#type获取数据类型
print(x)

e = str(2333)
print(type(e))#把2333转换成str类型
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
print("0:代表偶数;1:代表奇数")
lstr = input("请输入您要计算的内容：")
print(len(lstr)%2)



# my_yuanzu = (1,2,3) #元组
# print(my_yuanzu)

# my_liebiao = [1,2,3,4,5,6] #列表
# print(my_liebiao)

# my_zidian = {"username":"liuyun", "password":"a123456"} #字典：json格式 键key 值value
# print(my_zidian)