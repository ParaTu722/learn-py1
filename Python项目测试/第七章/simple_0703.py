# 练习7-4

pizzas = "Please,输入一系列比萨配料:" \
        "\n\t输入'quit' 时退出!"
while True:
    pizza = input(pizzas)   # 此处易错点，input将字符pizzas显示，并有一个可输入变量pizza
    if pizza == 'quit':
        break
    else:
        print(f"我们会在比萨中添加{pizza}")


# 练习7-5：电影票
ages = "你的年龄是：" \
       "\n\t（输入quit即可退出！）"

while True:
    age = input(ages)
    if age == 'quit':
        break
    age = int(age)      # 字符转整型,17与19的顺序影响quit是否可以正确输入，因为有一个转int
    if age < 3:
        print("免费")
    elif age < 12:
        print("10CNY")
    elif age >= 12:
        print("15CNY")
'''
pizzas = "Please,输入一系列比萨配料:" \
        "\n\t输入'quit' 时退出!"
pizza = ""
active = True
while active:
    pizza = input(pizzas)
    if pizza == 'quit':
        active = False
    else:
        print(f"我们会在比萨中添加{pizza}")


ages = "你的年龄是：" \
       "\n\t（输入quit即可退出！）"
age = ""
active = True
while active:
    age = input(ages)
    if age == 'quit':   #与break退出不同
        active = False
    elif int(age) < 3:
        print("免费")
    elif int(age) < 12:
        print("10CNY")
    elif int(age) >= 12:
        print("15CNY")
'''