# 练习4-10

new_list = []
new_list.append('one')
new_list.append('two')
new_list.append('three')
new_list.insert(3, 'four')
new_list.insert(4, 'five')
print(f"The first three items in the list are:\n\t{new_list[:3]}")
print("---------------------------------")
print(f"Three items from the middle of the list are:\n\t{new_list[1:4]}")
print("---------------------------------")
print(f"The last three items in the list are:\n\t{new_list[-3:]}")

# 练习4-11

pizzas = []
pizzas.append('菠萝披萨')
pizzas.append('芝士披萨')
pizzas.insert(1, '火腿披萨')

friend_pizzas = pizzas[:]

pizzas.append('草莓披萨')
friend_pizzas.append('榴莲披萨')

for pizza in pizzas:
    print(f"My favorite pizzas are:{pizza}")
print("---------------------------------")
for friend_pizza in friend_pizzas:
    print(f"My friend favorite pizzas are:{friend_pizza}")
print("---------------------------------")
print("---------------------------------")

# 练习4-13
restaurants = ('红烧肉', '宫保鸡丁', '油泼面', '大烩菜', '口水鸡')
print("这里有：")
for restaurant in restaurants:
    print(f"\t{restaurant}")
# restaurants[0]='鱼香肉丝'  不能给元组的元素赋值
print("这现在里有：")
restaurants = ('红烧肉', '宫保鸡丁', '油泼面')
for restaurant in restaurants:
    print(f"\t{restaurant}")