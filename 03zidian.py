a = {"name":"零零零","password":"000"} #键值对 键（key） 值（value）  {key:value}

"""
字典没有下标的概念 说明了 字典没有顺序的说法
字典取值 靠key
"""

#字典取值:
# print(a["name"]) #通过key值来取--当key不存在时会报错
# print(a.get("name"))#通过get的方式来取值--当key不存在时不会报错，会返回none，更安全

# print(a["hh"]) #如果键不存在，这种方式报错
# print(a.get("hh")) #这种方式不报错

#修改
a["name"] = "零零"
print(a)

#第二种方法 修改 （复杂）
a.update({"name":"嘻嘻零"})
print(a)

#添加
#第一种方法
a.update({"sex":"女"}) #update的写法，key在这里是一个变量的写法
#a.update(address="成都")
print(a)

#第二种方法
a["age"] = 18 #当key不存在时，就会新增，当key存在时，就修改原值为现在的值
print(a)

#取走
# a.pop("sex")
# print(a)

#通用的删除方法，可以删字典，可以删数组
# del a["sex"]
# print(a)

print(list(a.keys())) #把所有的key值取出来并组成一个数组
print(list(a.values())) #把所有的value值取出来并组成一个数组