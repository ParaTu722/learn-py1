"""练习10-11：喜欢的数 　编写一个程序，提示用户输入喜欢的数，并使用
json.dump() 将这个数存储到文件中。再编写一个程序，从文件中读取这个
值，并打印如下所示的消息"""

import json


def save_data():
    """存数据"""
    with open(filename, 'w') as f:
        json.dump(number, f)
        print("Thanks! I'll remember that.")


def read_data():
    """读数据"""
    with open(filename) as f:
        show_nums = json.load(f)
    print(f"I know your favorite number! It's {number}.")


number = input("请输入喜欢的数:")
filename = 'like_number.json'
save_data()
read_data()
