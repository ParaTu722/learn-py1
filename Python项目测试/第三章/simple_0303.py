# 使用方法pop()删除元素
# 方法pop()可删除列表末尾的元素，并让你能够接着使用它
fruit = ['apple', 'pear', 'banana', 'watermelon']
print(fruit)
popped_fruit = fruit.pop()
print(fruit)
print(popped_fruit)

# 实际上，你可以使用pop()来删除列表中任何位置的元素，只需在括号中指定要删除的元素的索引即可
popped_fruit = fruit.pop(1)
print(f"我吃了{popped_fruit}!")
