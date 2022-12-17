# 10.2 写入文件

# 10.2.1 写入空文件
filename = 'text_files/programming.txt'
with open(filename, 'w') as file_object:
    # 调用open() 时提供了两个实参:一个是文件名;另一个是'w'即以写入模式打开这个文件
    # open()时,可指定读取模式（'r'）、写入模式（'w'）、附加模式'a')或读写模式（'r+'）
    # 如果省略了模式实参，Python将以默认的只读模式打开文件
    # 如果要写入的文件不存在，函数open()将自动创建它
    # 如果指定的文件已经存在，Python将在返回文件对象前清空该文件的内容
    file_object.write("I love programming.")
    """
      Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，
    必须先使用函数str()将其转换为字符串格式。
    """

# 10.2.2 写入多行
    file_object.write("I love creating new games.\n")
    # 此时两个内容会连在一起，所以需要在方法调用write() 中包含换行符
    file_object.write("------------------------\n")
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# 10.2.3 附加到文件,以附加模式 打开文件
# 以附加模式打开文件时，Python不会在返回文件对象前清空文件的内容，而是将写入文件的行添加到文件末尾。如果指定的文件不存在，Python将为你创建一个空文件
with open(filename, 'a') as file_object_02:
    file_object_02.write("------------------------\n")
    file_object_02.write("I also love finding meaning "
                         "in large datasets.\n")
    file_object_02.write("I love creating apps that "
                         "can run in a browser.\n")