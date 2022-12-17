# 列表排序

# 方法sort(),是按字母顺序排列从小到大,永久性地修改
cars = ['plane', 'car', 'train', 'boat']

'''
cars.sort()
print(cars)

# 还可以按与字母顺序相反的顺序排列列表元素，只需向sort() 方法传递参数 reverse=True
cars.sort(reverse=True)
print(cars)

'''
#  使用函数sorted() 对列表临时排序
print(f"交通工具有:{sorted(cars)}")
print(f"交通工具现在有:{cars}")

# !!!reverse() 不是按与字母顺序相反的顺序排列列表元素，而只是反转列表元素的排列顺序
# 方法reverse() 永久性地修改列表元素的排列顺序，但可随时恢复到原来的排列顺序，只需对列表再次调用reverse() 即可。
cars.reverse()
print(f"我这只是反转现有顺序：{cars}")
# 使用函数len() 可快速获悉列表的长度。
print(len(cars))