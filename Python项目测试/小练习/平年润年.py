# 输入一个年份和月份，判断平年闰年和月份天数
year = int(input("请输入一个年份："))
month = int(input("请输入一个月份："))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("今年是闰年")
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        print("这个月有31天")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        print("这个月有30天")
    elif month == 2:
        print("这个月有29天")
    else:
        print("月份输入错误！！！")
else:
    print("今年是平年")
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        print("这个月有31天")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        print("这个月有30天")
    elif month == 2:
        print("这个月有28天")
    else:
        print("月份输入错误！！！")