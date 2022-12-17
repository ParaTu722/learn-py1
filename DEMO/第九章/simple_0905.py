# 9.5 Python标准库

from random import randint, choice

# 它将两个整数作为参数，并随机返回一个位于这两个整数之间（含）的整数
num = randint(1, 77)
print(num)


# 它将一个列表或元组作为参数，并随机返回其中的一个元素
player = ['charles', 'martina', 'michael', 'florence', 'eli']
item = choice(player)
print(item)

