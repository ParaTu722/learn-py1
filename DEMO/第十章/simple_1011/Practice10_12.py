"""练习10-12：记住喜欢的数 　将练习10-11中的程序合二为一。如果存储了用户
喜欢的数，就向用户显示它，否则提示用户输入喜欢的数并将其存储到文件
中。运行这个程序两次，看看它能否像预期的那样工作。"""
import json


def read_data():
    """存数据就读取"""
    filename = 'like_number.json'
    try:
        with open(filename, 'r') as f:
            numbers = json.load(f)
    except FileNotFoundError:
        print('file not found\n')
    else:
        return numbers


def save_data():
    """未存储则提示用户输入喜欢的数并将其存储到文件"""
    filename = 'like_number.json'
    number = input("请输入喜欢的数:")
    with open(filename, 'w') as f:
        json.dump(number, f)
    return number


def greet_user():
    """判断用户是否存了数据"""
    number = read_data()
    if number:
        print(f"I know your favorite number! It's{number}")
    else:
        number = save_data()
        print(f"i will remember you num")


# greet_user()

# 答案写法,代码思路对比，简洁

filename = 'like_number.json'
try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("请输入喜欢的数:")
    with open(filename, 'w') as f:
        json.dump(number, f)
    print("Thanks, I'll remember that.")
else:
    print(f"I know your favorite number! It's {number}.")

#读取文件内容，有一个变量等于你读到的内容