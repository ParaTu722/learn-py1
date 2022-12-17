# 练习10-6：加法运算
def add_calculator():
    """加法运算"""
    try:
        a = int(input("请输入一个数："))
        b = int(input("请输入另一个数："))
    except ValueError:
        print("输入整数而不是文本\n")
    else:
        count = a + b
        print(count)


# 练习10-7：加法计算器
def new_add_calculator():
    """加法运算"""
    print("Enter 'q' at any time to quit.\n")
    while True:
        try:
            a = input("请输入一个数：")
            if a == 'q':
                break
            a = int(a)
            b = input("请输入另一个数：")
            if b == 'q':
                break
            b = int(b)
        except ValueError:
            print("输入整数而不是文本\n")
        else:
            count = a + b
            print(count)


# 练习10-8：猫和狗
"""
def creat_dog_and_cat():
    filename1 = 'text_files/dog.txt'
    with open(filename1, 'w') as cd:
        cd.write("sim bob pop nice ")
    filename2 = 'text_files/cat.txt'
    with open(filename2, 'w') as cc:
        cc.write("jim red fff milk ")

def show_dog_and_cat():
    filename1 = 'text_files/dog.txt'
    filename2 = 'text_files/cat.txt'
    with open(filename1, 'r') as cd:
        show_dog = cd.read()
        print(show_dog)
    with open(filename2, 'r') as cc:
        show_cat = cc.read()
        print(show_cat)
"""

filenames = ['text_files/cat.txt', 'text02.txt', 'text_files/dog.txt']
for filename in filenames:
    print(f"\nReading file: {filename}")
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print(" Sorry, I can't find that file.")
        # 练习10-9：静默的猫和狗
        # pass

print('\n------------------------------------\n')

# 练习10-10：常见单词
line = "Row , row , row your boat"
num1 = line.count("row ")
print(num1)
num2 = line.lower().count("row ")
print(num2)

print('\n------------------------------------\n')

files = ['text_files/text.txt', 'text03.txt', 'text_files/dog.txt']
for file in files:
    try:
        with open(file, 'r') as fi:
            content = fi.read()
    except FileNotFoundError:
        print(" Sorry, I can't find that file.")
    else:
        numword = content.split()
        print(len(numword))
        num3 = content.lower().count('the ')
        print(num3)
        num3 = content.lower().count('apple ')
        print(num3)