
res(1,2,3,4)
try:
    res[30]
    print("111")
except:
    print("222")   #如果try里面代码报错，就执行except里面的代码（但如果except里面也报错 代码就直接终止）



res(1,2,3,4)
try:                #最先运行
    res[30]
    print("111")
except:             #报错之后运行
    print("222") 
else:               #没有报错运行
    print("333")
finally:            #无论如何，最后都要运行
    print("444")  