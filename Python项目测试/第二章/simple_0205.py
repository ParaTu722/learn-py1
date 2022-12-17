# 基本运算 + - * /
print(5+4)
print(15-6)
print(3*3)
print(27/3)

age = 23
message = f"Happy {str(age)} rd Birthday!"
# message = "Happy "+age+"rd Birthday!"
# 可调用函数str()，它让Python将非字符串值表示为字符串

print(message)

# 多个变量赋值
a, b, c = 1, 2.2, "runoob"
print(a, b, c)
print(type(a))      # 内置的 type() 函数可以用来查询变量所指的对象类型。
isinstance(a, int)  # 通过ture/false判断变量所指的对象类型

ONE_COUNT =1715
print(ONE_COUNT)