# 5.3 if语句

# 5.3.1-2 简单的if语句
age = 17
if age >= 19:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
print("-------------------------------------")
print("-------------------------------------")

# 5.3.3 if-elif-else 结构
'''
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
'''
# 更简洁代码,也使用多个 elif 代码块
age = 26
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 30:
    price = 35
elif age < 60:
    price = 45
else:
    price = 55
print(f"Your admission cost is ${price}.")
print("-------------------------------------")
print("-------------------------------------")

# 5.3.5 省略else 代码块
'''
else 是一条包罗万象的语句，只要不满足任何if 或elif 中的条件测试，其中的
代码就会执行。这可能引入无效甚至恶意的数据。如果知道最终要测试的条件，应
考虑使用一个elif 代码块来代替else 代码块。这样就可以肯定，仅当满足相应的
条件时，代码才会执行。
'''
age = 80
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 30:
    price = 35
elif age < 60:
    price = 45
elif age >= 60:
    price = 55
print(f"Your admission cost is ${price}.")

print("-------------------------------------")
print("-------------------------------------")
# !!!!对于以上的if语句都只能满足一个条件，满足后则会跳出整个语句




# 5.3.6 测试多个条件
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:   # in 检查元素在不在列表中
    print("\tAdding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("\tAdding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("\tAdding extra cheese.")
print("Finished making your pizza!")

print("-------------------------------------")
print("-------------------------------------")
# 如果像下面这样转而使用if-elif-else 结构，代码将不能正确运行，因为有一个测试通过后，就会跳过余下的测试
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("\tAdding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("\tAdding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("\tAdding extra cheese.")
print("Finished making your pizza!")


print("-------------------------------------")
print("-------------------------------------")
print("-------------------------------------")
print("-------------------------------------")

# 练习5-3,5-4：外星人颜色
alien_color = 'red'
if alien_color == 'green':
    print("Player,you get 5 scores.")
else:
    print("Player,you get 10 scores.")
print("-------------------------------------")

# 练习5-5
new_alien_color = 'red'
if new_alien_color == 'green':
    print("Player,you get 5 scores.")
elif new_alien_color == 'yellow':
    print("Player,you get 10 scores.")
else:
    print("Player,you get 15 scores.")
print("-------------------------------------")

# 练习5-6
new_age = 65
if new_age < 2:
    print('Is a baby.')
elif new_age < 4:
    print('幼儿')
elif new_age < 13:
    print('儿童')
elif new_age < 20:
    print('青少年')
elif new_age < 65:
    print('成年人')
else:
    print('老年人')

print("-------------------------------------")
# 练习5-7
fruit = []
fruit.append('apple')
fruit.append('banana')
fruit.append('pear')
fruit.append('watermelon')

if 'apple' in fruit:
    print("You really like apples!")
if 'banana' in fruit:
    print("You really like bananas!")
if 'pear' in fruit:
    print("You really like pears!")
if 'watermelon' in fruit:
    print("You really like watermelons!")
if 'lemon' in fruit:
    print("You really like lemons!")
    # 注意5.3.6出现的错误