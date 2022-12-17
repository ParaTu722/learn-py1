# 删除空白
name = " albert einstein "
print(name)

print(name.rstrip())    #删除句末空格
print(name.lstrip())    #删除句首空格
print(name.strip())     #删除两端空格

# 这种删除只是暂时的，接下来再次打印name时还是原样，所有要想永久删除必须将之存到变量中
'''
name = name.rstrip()
'''

print("------------------------")
# 添加制表符，可使用字符组合\t
# 要在字符串中添加换行符，可使用字符组合\n
name1 = "java"
name2 = "c"
name3 = "python"
print(f"My Favorite languages is:\n\t{name1.title()}\n\t{name2.title()}\n\t{name3.title()}")