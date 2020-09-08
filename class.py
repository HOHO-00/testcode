
#定义好的类是没有任何作用的
class Person(): #类名和方法名，可以随便取（不能数字和特殊字符开头），（类名不成文规定）驼峰命名：英文首字母大写
    #属性：类的成员变量（实例变量）
    name = "零零"
    age = "18"
    sex = "女"

    #功能:成员方法  第一个参数必须要用self关键字开头
    def fly(slef):
        print("00fly")
    def high(self,yeah):
        # self.fly()  #self还可以调用成员方法  类里面相互调方法：一定要用self
        self.yz = "nice"  #这个成员属性一定是不存在的，才会去创建
        print("{}lalala,{}".format(self.name,yeah))

#实例化：创建类的对象：Person()：对象(可理解为把柄)
p = Person()
print(p.name)
print(p.age)
print(p.sex)
print(p.fly())  #成员方法的self不用传参
p.high("xixixi")
print(p.yz)