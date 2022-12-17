# 8.2.4 等效的函数调用
'''
# 一条名为Willie的小狗。
describe_pet('willie')
describe_pet(pet_name='willie')
# 一只名为Harry的仓鼠。
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
'''
# 8.2.5 避免实参错误
# 你提供的实参多于或少于函数完成工作所需的信息时，将出现实参不匹配错误
'''
def describe_pet(animal_type, pet_name):
    """显示宠物的信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet()
会报错
'''

# 练习
# 练习8-3/4：T恤
def make_shirt(size, picture='I love Python'):
    """T恤的尺码和图案"""
    print(f"我想要一件{size.title()}尺寸的T恤。")
    print(f"\t上面印着{picture}的图案。")
make_shirt('l')
make_shirt(size='m', picture='dog')
print('-----------------------------------------------------')
print('-----------------------------------------------------')

# 练习8-5：城市
def describe_city(city, country='china'):
    """一座城市名以及所属国家"""
    print(f"{city.title()} is in {country.title()}.")
describe_city(city='beijin')
describe_city(country='usa', city='jlfny')
print('-----------------------------------------------------')
print('-----------------------------------------------------')


# 8.3 返回值
# 函数并非总是直接显示输出，它还可以处理一些数据，并返回一个或一组值。函数返回的值称为返回值
# 可使用return 语句将值返回到调用函数的代码行。

# 8.3.1 返回简单值
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名。"""
    full_name = f"\t{first_name} {last_name}"
    return full_name.title()
# 调用返回值的函数时，需要提供一个变量，以便将返回的值赋给它
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

print('-----------------------------------------------------')
print('-----------------------------------------------------')

# 8.3.2 让实参变成可选的
# 并将其形参默认值设置为空字符串
def new_get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名。"""
    if middle_name:
        # 检查是否提供了中间名.Python将非空字符串解读为True,因此如果函数调用中提供了中间名,if...将为True
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
new_musician = new_get_formatted_name('jimi', 'hendrix')
print(new_musician)
new_musician = new_get_formatted_name('jimi', 'hendrix', 'lee')
print(new_musician)