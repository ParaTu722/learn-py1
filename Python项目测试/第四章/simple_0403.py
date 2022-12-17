# 4.4 使用列表的一部分

# 4.4.1 切片,你还可以处理列表的部分元素，Python称之为切片
'''
  要创建切片，可指定要使用的第一个元素和最后一个元素的索引。与函数range()一样，
Python在到达第二个索引之前的元素后停止。要输出列表中的前三个元素，需要指定索引0和3，这将返回索引为0、1和2的元素。
'''

players = []
players.insert(0, 'bob')
players.insert(1, 'tom')
players.insert(2, 'jim')
players.insert(3, 'ming')
players.insert(4, 'jin')
print(players[0:3])     # 含前三名队员
print(players[1:4])     # 提取列表的第二、第三和第四个元素
print(players[:4])      # 如果没有指定第一个索引，Python将自动从列表开头开始
print(players[2:])      # 要让切片终止于列表末尾
print(players[-2:])      # 无论列表多长，这种语法都能够让你输出从特定位置到列表末尾的所有元素
print("---------------------------------")
print("---------------------------------")

# 4.4.2 遍历切片
# 有遍历整个队员列表
print("Here are the first three players on my team:")
for player in players:
    print(f"\t{player.title()}")
print("---------------------------------")
print("---------------------------------")
# 有遍历1-3队员
print("again Here are the first three players on my team:")
for player in players[1:4]:
    print(f"\t{player.title()}")

print("---------------------------------")
print("---------------------------------")
# 4.4.3 复制列表

my_food = ['apple', 'pizaa', 'banana', 'fish']
myfriend_food = my_food[:]

my_food.append('beaf')
myfriend_food.append('chicken')

print(f"My favorite foods are:\n\t{my_food}")
print(f"My friend favorite foods are:\n\t{myfriend_food}")

'''
# 这种语法实际上是让Python将新变量friend_foods关联到已与my_foods 相关联的列表，因此这两个变量指向同一个列表。
my_food = ['apple', 'pizaa', 'banana', 'fish']
myfriend_food = my_food

my_food.append('beaf')
myfriend_food.append('chicken')

print(f"My favorite foods are:\n\t{my_food}")
print(f"My friend favorite foods are:\n\t{myfriend_food}")

'''