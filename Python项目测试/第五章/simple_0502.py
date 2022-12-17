# 练习5-1：条件测试

cars = 'subaru'
# cars = 'audi'
if cars == 'subaru':
    print("Is car == 'subaru'? I predict True.")
    print("cars == 'subaru'")
else:
    print("Is car == 'subaru'? I predict False.")
    print("cars == 'audi'")
print('------------------------------')

# 练习5-2：更多条件测试
number_0 = 'two'
number_1 = 'Two'
if number_0 == number_1.lower():
    print("True")
else:
    print("False")

print('------------------------------')

age_0 = 21
age_1 = 22
if age_0 <= 20 and age_1 >=22:
    print("true")
else:
    print("false")
print("-------------------------------------")
age_0 = 16
age_1 = 22
if age_0 <= 20 or age_1 >=23:
    print("true")
else:
    print("false")

print("-------------------------------------")
# 5.2.5 , 检查特定值是(可使用关键字in),否(可使用关键字not in)包含在列表中
users = ['andrew', 'carolina', 'david']
user_0 = 'andrew'
user_1 = 'tom'
if user_0 in users:
    print(f"{user_0.title()},you can post a response")
if user_1 not in users:
    print(f"{user_1.title()},you can not post a response")
print("-------------------------------------")