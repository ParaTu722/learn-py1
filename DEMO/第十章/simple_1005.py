# 10.3 异常

# Python用称为 异常 的特殊对象来管理程序执行期间发生的错误
# 异常是使用try-except 代码块处理的
# 使用try-except 代码块时，即便出
# 现异常，程序也将继续运行

"""
print(5/0)

Traceback (most recent call last):
  File "F:\CODE\DEMO\第十章\simple_1005.py", line 8, in <module>
    print(5/0)
ZeroDivisionError: division by zero

    ZeroDivisionError 是个异常对象
"""

# 10.3.2 使用try-except 代码块
# 当你认为可能会发生错误时，可编写一个try-except 代码块来处理可能引发的异常
try:
    print(5 / 0)
    print(5 / 2)    # 将正常计算结果
except ZeroDivisionError:
    print("不能除以0\n")

"""
    如果try 代码块中的代码运行起来没问题，Python将跳过except代码块；
    若try代码块中的代码有错误，Python将查找与之匹配的except 代码块并运行其中的代码
"""

# 10.3.3 使用异常避免崩溃
# 来创建一个只执行除法运算的简单计算器
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_num = input("\t输入被除数：")
    if first_num == 'q':
        break
    second_num = input("\t输入除数：")
    if second_num == 'q':
        break
    try:
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print("不能除以0\n")
    # 依赖try 代码块成功执行的代码都放在else 代码块中
    else:
        print(answer)