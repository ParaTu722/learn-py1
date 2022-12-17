# 8.5 传递任意数量的实参
def make_pizza(*toppings):
    # 形参名*toppings中的*让Python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组中
    """打印顾客点的所有配料。"""
    print("Making a pizza with the following toppings:")
    for topping in toppings:
        print(f"\t{topping}")
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

print('-------------------------------------------------------')
print('-------------------------------------------------------')


# 8.5.1 结合使用 位置实参和任意数量实参
"""
  如果要让函数接受不同类型的实参，必须在函数定义中将 接纳任意数量实参的形参 放在最后。
Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中
"""
def make_pizza(size, *toppings):
    # 形参名*toppings中的*让Python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组中
    """打印顾客点的所有配料。"""
    print(f"Making a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"\t{topping}")
make_pizza('12', 'pepperoni')
make_pizza('6', 'mushrooms', 'green peppers', 'extra cheese')
# 你经常会看到通用形参名*args ，它也收集任意数量的位置实参

print('-------------------------------------------------------')
print('-------------------------------------------------------')




# 8.5.2 结合使用任意数量的 关键字实参
def build_profile(first, last, **user_info):
    # 形参**user_info 中的两个星号让Python创建一个名为user_info的空字典，并将收到的名称值对都放到字典中,（区别于19行，创建的是空元组）
    """创建一个字典，其中包含我们知道的有关用户的一切。"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info    # 将字典user_info 返回到函数调用行
user_profile = build_profile('张', '三', location='厦门', field='物理')
print(user_profile)
# 你经常会看到形参名**kwargs ，它用于收集任意数量的关键字实参(区别于位置实参)

print('-------------------------------------------------------')
print('-------------------------------------------------------')
print('-------------------------------------------------------')
print('-------------------------------------------------------')


# 练习8-12：三明治
def sandwich(size, *toppings):
    """接受顾客要在三明治中添加的一系列食材"""
    print(f"您点的{size}三明治中包含了：")
    for topping in toppings:
        print(f"\t{topping}")
sandwich('big', 'pepperoni', 'banana')
sandwich('small', 'mushrooms', 'green peppers', 'extra cheese')
sandwich('huge', 'green peppers')
print('-------------------------------------------------------')
print('-------------------------------------------------------')

# 练习8-13：用户简介
my_profile = build_profile('王', '五', location='厦门', school='集美', field='物理')
print(my_profile)
print(f"\t大家好，我的名字是{my_profile['first_name']}{my_profile['last_name']}，"
      f"我在{my_profile['location']}的{my_profile['school']}学校学习{my_profile['field']}")
print('-------------------------------------------------------')
print('-------------------------------------------------------')





# 练习8-14：汽车

def make_car(manufacturer, model, **car_inform):   #(制造商，型号，其他车辆信息)
    """一辆汽车的信息"""
    car_inform['manufacturers'] = manufacturer
    car_inform['models'] = model
    return car_inform
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
manufacturer = input("请输入汽车制造商：")
model = input("请输入汽车的型号：")
car = make_car(manufacturer, model, color='blue', tow_package=True)
print(f"{car['manufacturers']}制造的{car['models']}型号的车，"
      f"颜色是{car['color']}，配件是{car['tow_package']}!!!")