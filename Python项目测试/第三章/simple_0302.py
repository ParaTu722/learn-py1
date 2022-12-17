# 列表元素的增，删，改
fruit = ['apple', 'pear', 'banana', 'watermelon']
print(fruit)
print("------------------------------")

'''
# 修改列表元素
fruit[0]='grape'
print(fruit)
print("------------------------------")
'''

# 在列表中添加元素
fruit.append('grape')   #将元素附加到列表末尾,用方法append()
print(fruit)
print("------------------------------")

# 以先创建一个空列表，再使用一系列的append()语句添加元素
new_fruits = []
new_fruits.append('pear')
new_fruits.append('watermelon')
new_fruits.append('grape')
print(new_fruits)
print("------------------------------")

# 在列表中插入元素
fruit.insert(0, 'strawberry')   #使用方法insert()可在列表的任何位置添加新元素
print(fruit)
print("------------------------------")

# 从列表中删除元素
del fruit[0]    #将刚刚添加的草莓删除了
del fruit[1]    #因为草莓已删除，所以【0】是苹果，【1】是pear
print(fruit)