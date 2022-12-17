# 10.3.5 处理FileNotFoundError 异常

"""
filename = 'alice.txt'
with open(filename, encoding='utf-8') as f:
    contents = f.read()

  相比于本章前面的文件打开方式，这里有两个不同之处。
  一是使用变量f 来表示文件对象，这是一种常见的做法。
  二是给参数encoding 指定了值，在系统的默认编码与要读取文件使用的编码不一致时，必须这样做
"""

# FileNotFoundError 异常，这是Python找不到要打开的文件时创建的异常

filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"sorry ,{filename} not found")

print("\n----------------------------\n")
# 10.3.6 分析文本
tittles = "Alice in Wonderland"
tittle = tittles.split()
print(tittle)
print(len(tittle))
print("----------------------------\n")
def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename, encoding='utf-8') as fI:
            contents = fI.read()
    except FileNotFoundError:
        # print(f"sorry , {filename} not found")
        pass
    else:
        # 计算该文件大致包含多少个单词。
        words_list = contents.split()
        words_len = len(words_list)
        print(f"{filename} has about {words_len} words")


count_words('text_files/text.txt')
count_words('alice.txt')

print("----------------------------\n")

# 10.3.7 使用多个文件
filenames = ['alice.txt', 'text_files/text.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

print("----------------------------\n")
# 10.3.8 静默失败
# 将except FileNotFoundError:中执行的错误打印改成pass
# Python有一个pass 语句，可用于让Python在代码块中什么都不要做