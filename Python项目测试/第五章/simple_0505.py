# 练习练习5-8，5-9
users = ['bob', 'tom', 'admin', 'scc', 'ming', 'ling']
# users = []
if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"\tHello {user.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")

# 如何利用for循环，高效率删除列表值？？？？
print('---------------------------------------------------')
print('---------------------------------------------------')

# 练习练习5-10
current_users = ['bob', 'tom', 'admin', 'scc', 'ming', 'ling']
new_users = ['smith', 'tom', 'jack', 'keven', 'admin']

#  列表解析!!!!!!!!加强运用
current_users_lower = [current_user.lower() for current_user in current_users]

for new_user in new_users:
    if new_user in current_users:
        print(f"\t对不起,用户名{new_user.title()}已被使用！")
    else:
        print(f"用户名{new_user.title()}为新，可以使用")

# 练习练习5-11

#  列表解析 numbers = [value for value in range(1, 11)]
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        #如果用 if number == '1':则全都打印的是th，因为单引号里为字符，而使用list生成列表为值
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")