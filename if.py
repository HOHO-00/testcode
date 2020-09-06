# python的语句
# if：条件语句
a = 20

if a > 18:
    print("成年人，不能早睡")
else:
    print("未成年，可以早睡")

# > <
# >= <=


# 字符串条件 in，判断某个字符串是否在另外一个字符串中
t = "你两还争风吃醋上了"
y = "争风吃醋"
if y in t:
    print("y在t中，确实是在吃醋")
else:
    print("不在呗")

b = 123
c = 123
if b == c:
    print("b=c")
else:
    print("b不等于c")


# 多条件:长度为3个字儿，名字：大雁塔
# name = input("请输入白素贞被关押的塔名儿：")
# if name == "大雁塔" and len(name) == 3:
#     print("恭喜您的朋友，去吧")
# else:
#     print("不好意思，没对")

# if name == "雷峰塔" or len(name) == 5:
#     print("对了")
# else:
#     print("错了")

# if的嵌套
name = input("请输入白素贞被关押的塔名儿：")
# if name == "大雁塔":
#     if len(name) == 3:
#         print("对了")
#     else:
#         print("错了")
# else:
#     print("错了")

# if len(name) == 3:
#     if name == "大雁塔":
#         print("俺对了")
#     else:
#         print("我错了2")
# else:
#     print("我错了1")

a = 30
if a > 18:                          # a > 18
    print("成年人")
elif a > 16:                        # a > 16 and a < 18
    print("青年小伙伴")
elif a > 14:                        # a > 14 and a < 16
    print("少年小伙伴")
elif a > 6:                         # = a >6 and a < 14
    print("xxxx小伙伴")
else:                               # = a <=6
    print("这是啥，编不出来了")


if a > 18:
    print("111")
else:
    if a > 16:
        print("11")
    if a > 14:
        print("222")


# 作业：
# 1. 把代码用vscode抄三遍  （基础）
# 进阶：
# 2.输入一个账号，输入一个密码，要求判断账号的长度大于5位，并且小于8位，
# 如果输入账号为张三12345，密码为123456就可以登录成功，否则就登录失败

xm = input("请输入账号：")
mm = input("请输入密码：")
if len(zh) > 5 and len(zh) < 8:
    print("账号长度合法")
    if zh == "张三12345" and mm =="123456":
        print("登录成功")
    else:
        print("登录失败，账号或密码错误")
else:
    print("账号的长度不合法")