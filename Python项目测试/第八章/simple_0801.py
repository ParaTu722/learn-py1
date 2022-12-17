# 8.1 定义函数

# 使用关键字def 来告诉Python，你要定义一个函数。这是函数定义 ，向Python指出了函数名，还可能在圆括号内指出函数为完成任务需要什么样的信息
# 向函数传递信息，为此，可在函数定义def greet_user() 的括号内添加username
# def前要有两行空行，不然会有波浪线警告
def greet_user(username):
    # 文档字符串 （docstring）的注释，描述了函数是做什么的
    """显示简单的问候。"""
    # 执行的代码
    print(f"Hello!{username}")
greet_user('bob'.title())   # 函数调用

# 实参（bob）和形参（username）
print('-------------------------------------------')
print('-------------------------------------------')

# 练习8-1：消息


def display_message():
    """指出在本章学的是什么"""
    print("def")
display_message()
print('-------------------------------------------')
print('-------------------------------------------')

# 练习8-2：喜欢的图书


def favorite_book(title):
    """喜欢的图书"""
    print(f"One of my favorite books is 《{title}》.")
favorite_book('水浒传')
print('-------------------------------------------')
print('-------------------------------------------')

# 8.2 传递实参
# 8.2.1 位置实参:求实参的顺序与形参的顺序相同


def describe_pets(animal_type, pet_name):
    """显示宠物信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pets('hamster', 'harry')
# 多次调用函数
describe_pets('dog', 'willie')
# 实参的顺序很重要,不然打印结果有偏差,所以请确认函数调用中实参的顺序与函数定义中形参的顺序一致
print('-------------------------------------------')
print('-------------------------------------------')

# 8.2.2 关键字实参
'''
  是传递给函数的名称值对。因为直接在实参中将名称和值关联起来，所以
向函数传递实参时不会混淆(不会得到名为Hamster的harry这样的结果)。关键
字实参让你无须考虑函数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途。
'''
def describe_pet(animal_type, pet_name):
    """显示宠物的信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(animal_type='hamster', pet_name='harry')
# 关键字实参的顺序无关紧要
describe_pet(pet_name='harry', animal_type='hamster')

print('-------------------------------------------')
print('-------------------------------------------')

# 8.2.3 默认值
'''
编写函数时，可给每个形参指定默认值 。在调用函数中给形参提供了实参时，
Python将使用指定的实参值；否则，将使用形参的默认值。因此，给形参指定默认
值后，可在函数调用中省略相应的实参。使用默认值可简化函数调用，还可清楚地
指出函数的典型用法
'''
def pet(name, type='cat'):
    """显示宠物的信息。"""
    print(f"\n---I have a {type}.")
    print(f"---My {type}'s name is {name.title()}.")
pet(name='willlie')

# 最简单方式是在函数调用中只提供名字
pet('willlie')

# 也可以修改实参来改变默认值
pet(name='cc', type='dog')