# 7.1 函数input() 的工作原理
'''
message = input("Tell me something, and I will repeat it back to you: ")
print(message)


# 创建多行字符串的方式。
# 第一行将消息的前半部分赋给变量prompt中。在第二行中，运算符+= 在前面赋给变量prompt 的字符串末尾附加一个字符串。
# 最终的提示占据两行，且问号后面有一个空格
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)    # 使用函数input() 时，Python将用户输入解读为字符串
print(f"Hello, {name}!")
print("------------------------------------------------")
print("------------------------------------------------")

#7.1.2 使用int() 来获取数值输入
height = input("How tall are you, in inches? ")
height = float(height)    #  将输入转换成了数值表示,int整型，float浮点型
if height >= 48:
    print("\tYou're tall enough to ride!")
else:
    print("\tYou'll be able to ride when you're a little older.")
print("------------------------------------------------")
print("------------------------------------------------")

# 7.1.3 求模运算符
# 判断奇数偶数
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"\tThe number {number} is even.")
else:
    print(f"\tThe number {number} is odd.")

'''
# 练习7-1：汽车租赁
cars = "你想要什么车？"
cars += "我看看有没有货？"
car = input(cars)
print(f"\tLet me see if I can find you a {car}")
print("------------------------------------------------")
print("------------------------------------------------")

# 练习7-2：餐馆订位
peoples = input("有多少人用餐？")
peoples = int(peoples)
if peoples <= 8:
    print("\t有空桌")
else:
    print("\t没有空桌")
print("------------------------------------------------")
print("------------------------------------------------")

# 练习7-3：10的整数倍

numbers = input("输入一个数:")
numbers = int(numbers)
if numbers % 10 == 0:
    print("\t是10的整数倍")
else:
    print("\t不是10的整数倍")