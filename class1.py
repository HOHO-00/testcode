#类的继承

class Father():
    money = "1e"

    def make money(self):
        print("爸爸有个小目标")


# 类的继承：Son：子类：Father：父类
# 继承的好处：子类可以继承父类的属性和方法
class Son(Father):
    name = "sson"
    money = "-10e"
    def make_money(self):
        print("sson不要小目标了")


s = Son()
print(s.money)
s.make_money()