# 练习10-1：Python学习笔记
with open('text_files/learning_python.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())

print('-------------------------------')
print('-------------------------------')
with open('text_files/learning_python.txt') as file_object:
    for line in file_object:
        print(f"\t{line.rstrip()}")

print('-------------------------------')
print('-------------------------------')
with open('text_files/learning_python.txt') as file_object:
    contents = file_object.readlines()
for content in contents:
    print(content.rstrip())


print('-------------------------------')
print('-------------------------------\n')

# 练习10-2：C语言学习笔记
with open('text_files/learning_python.txt') as file_object_02:
    contents_02 = file_object_02.readlines()
for content_02 in contents_02:
    # 必须用 content_02 = content_02.replace....；不能直接.replace
    content_02 = content_02.replace('Python', 'C++')
    print(content_02.rstrip())