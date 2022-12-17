# 10.1 从文件中读取数据
# 10.1.1 读取整个文件


# 函数open()。要以任何方式使用文件，那怕仅打印内容，都得先打开文件，才能访问
# open() 接受一个参数：要打开的文件的名称
# open('xxx') 返回一个表示xxx文件的对象，Python将该对象赋给file_object 供以后使用

# 关键字with 在不再需要访问文件后将其关闭
with open('pi_digits.txt') as file_object:
    contents = file_object.read()

# print(contents)     # 输出唯一不同的地方是末尾多了一个空行
print(contents.rstrip())

print('---------------------------------------------')
print('---------------------------------------------\n')


# 10.1.2文件路径

# 方法1：要让Python打开不与程序文件位于同一个目录中的文件，需要提供文件路径

with open('text_files/filename.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())

print('---------------------------------------------')
print('---------------------------------------------\n')

# 显示文件路径时，Windows系统使用反斜杠（\ ）而不是斜杠（/ ）
# 应当改正

# 方法2：还可以将文件在计算机中的准确位置告诉Python，这称为《绝对文件路径》
file_path = 'C:/Users/15798/Desktop/苹果/file.txt'
with open(file_path) as file_object:
    contents = file_object.read()
print(contents.rstrip())


print('---------------------------------------------')
print('---------------------------------------------')
print('---------------------------------------------\n')


# 10.1.3 逐行读取

filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        # print(line.strip())
        if '8979323846' in line:
            print(line.strip())     # print(line)
        """
        为何会出现这些空白行呢？因为在这个文件中，每行的末尾都有一个看不见的换行
    符，而函数调用print() 也会加上一个换行符
        因此每行末尾都有两个换行符：一个来自文件，另一个来自函数调用print()
        """

print('---------------------------------------------')
print('---------------------------------------------')
print('---------------------------------------------\n')

# 10.1.4 创建一个包含文件各行内容的列表

filename_02 = 'pi_digits.txt'
with open(filename_02) as file_object_02:
    lines = file_object_02.readlines()
    # readlines() 从文件中读取每一行，并将其存储在一个列表中

for line in lines:
    print(line.rstrip())
print(lines)
print('---------------------------------------------\n')

# 10.1.5 使用文件的内容
pi_string1 = ''
pi_string2 = ''
for line in lines:
    pi_string1 += line.rstrip()
    pi_string2 += line.strip()
print(f"pi_string1: {pi_string1[0:10]}\tlen:{len(pi_string1)}")
# 遗忘点[0:10]，0到10位
# 为删除这些空格，可使用strip() 而非rstrip()
print(f"pi_string2: {pi_string2}\tlen:{len(pi_string2)}")
# 这个字符串长32字符，因为它还包含整数部分的3和小数点

# 10.1.7 圆周率值中包含你的生日吗
birthday = input("Enter your birthday: ")
if birthday in pi_string2:
    print('yes')
else:
    print('no')