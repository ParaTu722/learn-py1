# 4.1/4.2  for循环基础
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    # print(magician.title())
    print(f"oh my gid,amazing {magician.title()}!!!")
    print(f"see you again {magician.title()}.\n")
# 在for 循环后面，没有缩进的代码都只执行一次，不会重复执行
print(f"good night everybody!")
# for循环缩进很重要，冒号也不能忘记
print("---------------------------------")

# 练习4-1
pizzas = []
pizzas.append('菠萝披萨')
pizzas.append('芝士披萨')
pizzas.insert(1, '火腿披萨')
for pizza in pizzas:
    print(f"我非常喜欢吃:{pizza}")
print("\n披萨非常美味！！")
print("他们都由面粉制作！！")

# 4.3创建数值列表
# 4.3.1 使用函数range()
for value in range(0, 6):
    print(value)    # 只打印数1～5,这是编程语言中常见的差一行为的结果
print("---------------------------------")

# 4.3.2 使用range() 创建数字列表
numbers = list(range(0, 7))
print(numbers)
even_numbers = list(range(0, 12, 3))    # 还可指定步长
print(even_numbers)
print("---------------------------------")

'''
squares = []
for value in range(1,12):
    square = value**2
    squares.append(square)
print(squares)
'''
# 更简洁
squares = []
for value in range(1, 12):
    squares.append(value**2)
print(squares)

# 4.3.3 对数字列表执行简单的统计计算
# 可以轻松地找出数字列表的最大值、最小值和总和
digits = list(range(1, 99889))
print(f"min is:{min(digits)},\tmax is:{max(digits)},\tsum is:{sum(digits)}.")

# 4.3.4 列表解析
# 前面介绍的生成列表squares 的方式包含三四行代码，而列表解析让你只需编写一行代码就能生成这样的列表
# 列表解析 将for 循环和创建新元素的代码合并成一行，并自动附加新元素
new_spuares = [value**2 for value in range(1, 64, 4)]
print(new_spuares)