# 判断三角形，并计算面积
a = float(input("输入三角形三边长：\n"))
b = float(input("输入三角形三边长：\n"))
c = float(input("输入三角形三边长：\n"))
if a+b > c and a+c > b and c+b > a:
    s = (a + b + c) * 0.5
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    print(f"可以组成三角形，并且面积是：{s}")
else:
    print("不能组成三角形")
