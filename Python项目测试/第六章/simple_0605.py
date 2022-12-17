# 6.4 嵌套:将一系列字典存储在列表中，或将列表作为值存储在字典中

# 6.4.1 字典列表
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
print('--------------------------------------')
print('--------------------------------------')

#，使用range() 生成了30个外星人
aliens = []
for alien_number in range(30):
    new_aline = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_aline)
# print(aliens[:5]),不如for循环好看
for alien in aliens[:5]:
    print(alien)
print(f"一共创建了{len(aliens)}个外星人!")
print('--------------------------------------')
print('--------------------------------------')

# 可使用for 循环和if 语句来修改某些外形人的颜色。例如，要将前三个外星人修改为黄色、速度为中等且值10分
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
for alien in aliens[3:15]:
    if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
for alien in aliens[:20]:
    print(alien)
print('--------------------------------------')
print('--------------------------------------')

# 6.4.2 在字典中存储列表
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"{name.title()}'s favorite languages is:")
    else:
        print(f"{name.title()}'s favorite languages are"
              f":")
    for language in languages:
        print(f"\t{language.title()}")
print('--------------------------------------')
print('--------------------------------------')

# 6.4.3 在字典中存储字典
users = {
    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'location': 'china',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_inform in users.items():
    print(f"用户名是：{username.title()}")
    full_name = f"{user_inform['first']}{user_inform['last']}" # 拼接两个值，一起显示

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {user_inform['location'].title()}")

print('-------------------------------------------------------------------------')
print('-------------------------------------------------------------------------')
print('-------------------------------------------------------------------------')
print('-------------------------------------------------------------------------')

# 练习6-7：人们
infomations_1 = {}
infomations_1['first_name'] = '张'
infomations_1['last_name'] = '三'
infomations_1['age'] = '18'
infomations_1['city'] = '北京'

infomations_2 = {}
infomations_2['first_name'] = '李'
infomations_2['last_name'] = '四'
infomations_2['age'] = '25'
infomations_2['city'] = '天津'

infomations_3 = {}
infomations_3['first_name'] = '王'
infomations_3['last_name'] = '五'
infomations_3['age'] = '33'
infomations_3['city'] = '上海'

peoples = [infomations_1, infomations_2, infomations_3]
for people in peoples:
    # print(people)  这样显示更不美观
    print(f"大家好，我是{people['first_name']}{people['last_name']},"
          f"我今年{people['age']}岁,我来自{people['city']}！！")
print('-------------------------------------------------------------------------')
print('-------------------------------------------------------------------------')
print('-------------------------------------------------------------------------')
print('-------------------------------------------------------------------------')

# 练习6-8：宠物,与6.7类似
pets = []
pet = {
    'animal type': 'dog',
    'name': 'five',
    'owner': 'eric',
    'weight': '17',
    'eats': 'shoes',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'cola',
    'owner': 'ming',
    'weight': '38',
    'eats': 'fish',
}
pets.append(pet)

pet = {
    'animal type': 'cat',
    'name': 'jj',
    'owner': 'tom',
    'weight': '26',
    'eats': 'milk',
}
pets.append(pet)
for pet in pets:
    print(f"Here's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key.title()}: {value.title()}")

print('-------------------------------------------------------------------------')
print('-------------------------------------------------------------------------')
print('-------------------------------------------------------------------------')
print('-------------------------------------------------------------------------')

# 练习6-9：喜欢的地方
favorite_places = {
    'tom': ['beijing', 'xiamen', 'sanya'],
    'bob': ['zhangzhou', 'shandong'],
    'jim': ['beijing', 'xizang', 'taiyuan', 'xian'],
}
for name, places in favorite_places.items():
    print(f"{name.title()}喜欢的地方有:")
    for place in places:    #  如果用 print(f"{name.title()}喜欢的地方有:{places}") 则直接打印列表全部，不能修改大小写
        print(f"\t{place.upper()}")
print('-------------------------------------------------------------------------')
print('-------------------------------------------------------------------------')
print('-------------------------------------------------------------------------')
print('-------------------------------------------------------------------------')

# 练习6-10：喜欢的数2 　
numbers = {}
numbers['bob'] = [2, 3]
numbers['tom'] = [56, 1, 16]
numbers['jim'] = [900_000, 11]
numbers['ming'] = [84]
for new_name, like_nums in numbers.items():
    print(f"{new_name.title()} likes the following numbers:")
    for like_num in like_nums:
        print(f"\t{like_num}")
print('-------------------------------------------------------------------------')
print('-------------------------------------------------------------------------')
print('-------------------------------------------------------------------------')
print('-------------------------------------------------------------------------')

# 练习6-11：城市
cities = {
    '上海': {
        'country': '中国',
        'population': '200_0000',
        'fact': '金融中心',
    },
    '厦门': {
        'country': '中国，福建',
        'population': '100_0567',
        'fact': '风景宜人',
    },
    '烟台': {
        'country': '中国,山东',
        'population': '50_3590',
        'fact': '四季分明',
    },
}
for city, inform in cities.items():
    print(f"{city}这座城市：")

    country = inform['country']
    population = inform['population']
    fact = inform['fact']

    print(f"\t它属于：{country}，人口大约是：{population}，它的特点是：{fact}！！！")
    # print(f"\t{keys}:{values}")

