# 8.6 将函数存储在模块中
'''

Python读取这个文件时，代码行import simple_0806 让Python打开文件simple_0806.py，并将
其中的所有函数都复制到这个程序中。但是看不到复制的代码，它在运行时幕后进行
'''

# 8.6.2 导入特定的函数
from simple_0806 import sandwich
sandwich('small', 'mushrooms', 'green peppers', 'extra cheese')

# 8.6.3 使用as 给函数指定别名
from simple_0806 import sandwich as sh
sh('small', 'mushrooms', 'green peppers', 'extra cheese')

# 8.6.4 使用as 给模块指定别名
import simple_0801 as s1
s1.pet('hhh', 'cat')

# 8.6.5 导入模块中的所有函数
from simple_0801 import *
display_message()

import jieba