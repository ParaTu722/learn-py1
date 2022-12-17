# 练习10-3：访客
filename_01 = 'text_files/guest.txt'
names = input("请用户输入名字:")
with open(filename_01, 'w') as file_object_01:
    file_object_01.write(f"{names}\n")
with open(filename_01) as file_object_01:
    contents = file_object_01.read()
print(contents.rstrip())

print('--------------------------')
print('--------------------------\n')

# 练习10-4：访客名单
filename_02 = 'text_files/guest_book.txt'
names_02 = []
while True:
    name_02 = input("请用户输入名字:")
    print("\t欢迎欢迎\n")
    names_02.append(name_02)
    if name_02 == '0':
        names_02.remove('0')
        break
with open(filename_02, 'w') as file_object_02:
    for new_names_02 in names_02:
        file_object_02.write(f"{new_names_02}\n")
        file_object_02 .write("\t\tnew people!!!\n")

print('--------------------------')
print('--------------------------\n')

# 练习10-5：调查
filename_03 = 'text_files/reason.txt'
reasons = []
while True:
    reason = input("为什么喜欢编程:")
    reasons.append(reason)
    if reason == '0':
        reasons.remove('0')
        break
with open(filename_03, 'a') as file_object_03:
    for reason in reasons:
        file_object_03.write(f"{reason}\n")