# 8.3.3 返回字典（函数可返回任何类型的值）
# 新增了一个可选形参age ，并将其默认值设置为特殊值None,可将None 视为占位值。在条件测试中，None 相当于False
def build_person(first_name, last_name, age=None):
    """返回一个字典，其中包含有关一个人的信息。"""
    person = {
        'first': first_name,    # 存储first_name的值时,使用的键为first,last同理
        'last': last_name,
    }
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

print('-----------------------------------------------------')
print('-----------------------------------------------------')

# 8.3.4 结合使用函数和while 循环

def get_formatted_name(first_name, last_name):
    """返回整洁的姓名。"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("Please tell me your name:")
    print("\t(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\tHello, {formatted_name}!")