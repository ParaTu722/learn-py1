# 7.3 使用while 循环处理列表和字典

# 7.3.1 在列表之间移动元素

unconfirmed_users = ['alice', 'brian', 'candace']       # 首先创建一个未验证用户列表
confirmed_users = []        # 创建了一个空列表，用于存储已验证的用户

while unconfirmed_users:    # 的while 循环将不断运行，直到列表unconfirmed_users 变空
    current_user = unconfirmed_users.pop()      # 方法pop(),删除列表末尾元素，并接着使用

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
# 显示所有已验证的用户。
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

print('--------------------------------------------------')
print('--------------------------------------------------')

# 7.3.2 删除为特定值的所有列表元素
'''
  进入while 循环，发现'cat' 在列表中至少出现了一次。进入该循环后，
Python删除第一个'cat' 并返回到while 代码行，然后发现'cat' 还包含在列表
中，因此再次进入循环。它不断删除'cat' ，直到这个值不再包含在列表中
'''
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')      # 使用函数remove() 来删除列表中的特定值
print(pets)

print('--------------------------------------------------')
print('--------------------------------------------------')

# 7.3.3 使用用户输入来填充字典

# 创建一个空字典
responses = {}
# 设置一个标志，指出调查是否继续。
active = True
while active:
    # 提示输入被调查者的名字和回答
    name = input("What is your name?")
    response = input("Which mountain would you like to climb someday?")

    # 将回答存储在字典中。
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        active = False
# 调查结束，显示结果
print(responses)
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")