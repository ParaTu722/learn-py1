# 6.3 遍历字典

# 6.3.1 遍历所有键值对
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name, language in favorite_languages.items():
    print(f"\t{name.title()}'s favorite language is {language.title()}.")
'''
    要编写遍历字典的for 循环，可声明两个变量(name, language)，用于存储键值对中的键和值。这两个变量可以使用任意名称。
    for 语句的第二部分包含字典名和方法items()，它返回一个键值对列表。接下来，for 循环依次将每个键值对赋给指定的两个变量
'''
print('---------------------------------------------')
print('---------------------------------------------')

# 6.3.2 遍历字典中的所有键
# 在不需要使用字典中的值时，方法keys()很有用
for name in favorite_languages.keys():
# for name in favorite_languages: 替换,输出将不变
# 显式地使用方法keys() 可让代码更容易理解
    print(name.title())
print('---------------------------------------------')
print('---------------------------------------------')

friends = ['jen', 'phil']
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        languages = favorite_languages[name]
        print(f"\t{name.title()}, you favorite language is {languages.title()}")
    if name not in friends:
        print(f"{name.title()}  please take our poll!")

print('---------------------------------------------')
print('---------------------------------------------')

# 6.3.3 按特定顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print('---------------------------------------------')
print('---------------------------------------------')

# 6.3.4 遍历字典中的所有值,使用方法values() 来返回一个值列表，不包含任何键
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(f"\t{language.title()}")
# 为剔除重复项，可使用集合（set）,通过对包含重复元素的列表调用set() ，可让Python找出列表中独一无二的元素
print("剔除重复元素的列表：")
for language in set(favorite_languages.values()):
    print(f"\t{language.title()}")