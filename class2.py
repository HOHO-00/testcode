# 类-构造方法


class Hhh():

    # 构造方法：固定方法，类实例化的时候运行
    def __init__(self,xx):   #有一个类必然有一个_init_
        self.name = xx       #初始化了成员变量

    def aa(self):
        a = 1 # 只针对aa有效
        self.b = 2 # 对整个类有效

# 一定要去加参数
h = Hhh("000")  #实例化
print(h.name)