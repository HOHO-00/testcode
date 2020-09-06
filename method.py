# "ddd".format()  # 内置方法
# 自定义方法：为了重复使用
def add(s1=100,s2=200):
    sum = s1 + s2
    return sum

# a = 1 + 1
# b = 2 + 2

a = add(1, 1) # sum > sum = s1+s2
b = add(2, 2)
c = add()
# d = add(s2=1000, s1=20000) # 传参的时候给指定参数的值
print(a)
print(b)
print(c)


# def login(username, password):
#     a = 1
#     t_user = [{"username":"墩子", "password":"123456"}, {"username":"小玉", "password":"123456"}]
#     for i in t_user:
#         print('这是第{}次运行, i的值是{}'.format(a, i))
#         if u == i.get("username") and p == i.get("password"):
#             print("登陆成功！")
#             break  # 终止循环
#         else:
#             # 最后一次运行都还没有这个账号：再来打印登录失败
#             # 怎么来判断是最后一次运行 》 最后一次运行
#             if len(t_user) == a:
#                 print("登陆失败")
#         a = a + 1

# a123 = input("请输入账号:")
# b123 = input("请输入密码:")
# login(a123, b123) # login("小玉", "123456")


def paras_test(a, b, c):
    print(a)
    print(b)
    print(c)

a1 = [1,2,3]
a2 = (1,2,3)
a3 = {"1":"2", "2":"3"}
paras_test(a1, a2, a3)