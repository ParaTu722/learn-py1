# 10.4 存储数据
"""模块json 让你能够将简单的Python数据结构转储到文件中，并在程序再次运行时
加载该文件中的数据。你还可以使用json 在Python程序之间分享数据"""

# 10.4.1 使用json.dump() 和json.load()

import json

numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
    """
    先导入模块json ，再创建一个数字列表
    指定了要将该列表存到哪个文件中。常使用文件扩展名.json来指出文件存储的数据为JSON格式
    以写入模式打开这个文件，让json 能够将数据写入其中
    使用函数json.dump() 将数字列表存储到文件numbers.json中
    """
print('-----------------------------\n')
# 使用json.load() 将列表读取到内存中：
with open(filename, 'r') as f:
    numbers_1 = json.load(f)
    # 使用函数json.load() 加载存储在numbers.json中的信息，并将其赋给变量numbers
print(numbers_1)