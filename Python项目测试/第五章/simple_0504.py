# 5.4 使用if 语句处理列表

# 5.4.1 检查特殊元素
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':    #检查顾客是否点了青椒
        print("\tSorry, we are out of green peppers right now.")
    else:
        print(f"\tadding {requested_topping.title()}.")
print("Finished making your pizza!")

print('---------------------------------------------')

# 5.4.2 确定列表不是空的
requested_toppings = [] # 首先创建一个空列表
# 进行简单的检查，而不是直接执行for 循环。
# 在if 语句中将列表名用作条件表达式时，Python将在列表至少包含一个元素时返回True ，并在列表为空时返回False 。
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"\tadding {requested_topping.title()}.")
    print("Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

print('---------------------------------------------')

# 5.4.3 使用多个列表
# 比萨店供应的配料列表
available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
# 顾客点的配料列表
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"adding {requested_topping.title()}")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("Finished making your pizza!")