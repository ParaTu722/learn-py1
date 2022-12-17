# 5.1 一个简单if语句示例

cars = []
cars.append('audi')
cars.append('bmw')
cars.append('subaru')
cars.append('toyota')
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# 5.2.1 检查是否相等
# 5.2.2 检查是否相等时忽略大小写
# >>> car = 'bmw'
# >>> car == 'bmw'
# True
print("-------------------------------------")
# 5.2.3 检查是否不相等
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
print("-------------------------------------")
# 5.2.5
# 使用and 检查多个条件,要检查是否两个条件都为True ，可使用关键字and 将两个条件测试合而为一。
# 使用or检查多个条件,关键字or 也能够让你检查多个条件，但只要至少一个条件满足，就能通过
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

# 5.2.8 布尔表达式
# 布尔表达式的结果要么为True ，要么为False 。