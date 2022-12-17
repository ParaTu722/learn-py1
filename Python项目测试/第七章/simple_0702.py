# 7.2 while 循环简介
    # for 循环用于针对集合中的每个元素都执行一个代码块
    # 而while 循环则不断运行，直到指定的条件不满足为止

# 7.2.1 使用while 循环
'''

'''

current_numeber = 1
while current_numeber <= 5:
    print(f"\t{current_numeber}")
    current_numeber += 1    # 等价于current_numeber = current_numeber + 1

# 7.2.2 让用户选择何时退出
# 我们在其中定义了一个退出值 ，只要用户输入的不是这个值，程序就将接着运行
prompt = "输入一条消息：" \
         "\n当输入'quit' 即可退出！"
messag = ""
while messag != 'quit':
    messag =input(prompt)
    if messag != 'quit':
        print(f"\t{messag}")

# 7.2.3 使用标志
# 将变量active 设置为True ，让程序最初处于活动状态。这样做简化了while 语句，
# 因为不需要在其中做任何比较,相关的逻辑由程序的其他部分处理。只要变量active 为True ，循环就将继续运行
prompt = "输入一条消息：" \
         "\n当输入'quit' 即可退出！"
message = ""
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(f"\t{message}")

# 7.2.4 使用break 退出循环
prompt = "Please enter the name of a city you have visited:"
prompt += "\n\t(Enter 'quit' when you are finished.)"
while True:     # 以 while True: 打头的循环将不断运行，直到遇到break
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")


# 7.2.5 在循环中使用continue,
# 要返回循环开头，并根据条件测试结果决定是否继续执行循环，可使用continue语句，它不像break 语句那样不再执行余下的代码并退出整个循环
current_num = 0
while current_num < 23:
    current_num += 1    # 循环后，以步长1的方式往上数
    if current_num % 2 ==0:
        continue
    print(current_num)

# 7.2.6 避免无限循环 >> ctrl+F2 退出运行