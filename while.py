
# a = 10
# while a > 0:
#     print(a)
#     a = a - 1

# a = 10; > 10 ; a = 10 - 1 > 9
# a = 9; > 9; a = a - 1 > 8
# a = 8; > 8; a = 8-1 > 7
# a = 7; > 7; a = 6
# a = 6; > 6; a = 5
# a = 5; > 5; a = 4
# a = 4; > 4; a = 3
# a = 3; > 3; a = 2
# a = 2; > 2; a = 1
# a = 1; > 1; a = 0
# a = 0: 条件不满足，就不执行while  （循环退出的条件 就是while后面的条件）

# 有个list [80,60,59,29,99],来判断成绩是否合格，请把不合格的成绩打印出来
a = 0  # chengji的下标
chengji = [80,60,59,29,99,20,110]
while a < len(chengji):            # 如何去准确的获取到列表中的每个元素，而不落下
    if chengji[a] < 60:
        print("发现了一个壮士，啊哈哈哈，成绩是:{}".format(chengji[a]))   #format就是字符串的拼接格式化（把一个内容拼接到字符串后面）
    a = a + 1


# 红绿灯练习：红绿灯有60s，红灯35秒，绿灯20秒，黄灯5秒，红灯打印35次，绿灯打印20次，黄灯5次。
a = 0 
# while a < 60:
#     # 1-35：打印红灯
#     # 36-55：打印绿灯
#     # 56-60：打印黄灯
#     if a < 35: #0-34:35次红灯
#         print("俺是红灯")
#     if a > 34 and a < 55:# 35-54: 20次绿灯
#         print("俺是绿灯儿")
#     if a > 54 and a < 60:# 55-59:5次黄灯儿
#         print("俺是黄灯儿")

#     a = a + 1  # a = a-1

while a < 1:
    print("俺是死循环")