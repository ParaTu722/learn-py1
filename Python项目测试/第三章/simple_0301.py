fruit = ['apple', 'pear', 'banana', 'watermelon']
print(fruit)
print("-------------------------")
print(fruit[3])
print(fruit[0].title())     # 第一个列表元素的索引为0，而不是1

print(fruit[-1])    # 通过将索引指定为-1，可让Python返回最后一个列表元素,等同于fruit[3]


message = f"My Favorite fruit is {fruit[2]}"
print(message)


# 练习
names = ['scc', 'sjy', 'zsr', 'sxd', 'smh']
print(f"\t{names[0].upper()}")  # 与制表符 \t 结合，拼接变量
print(names[1].upper())
print(f"最近怎么样{names[0].upper()}？")
