# 练习6-4
glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs."
    }
for k, v in glossary.items():
    print(f"{k.title()}: {v.title()}")
print("-----------------------------------------")
print("-----------------------------------------")

# 练习6-5
rivers = {
    'china_0': 'changjiang',
    'china_1': 'huanghe',
    'india': 'niles',
    }
for country, river in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
for country in rivers.keys():
    print(f"国家有：{country.title()}.")
for river in rivers.values():
    print(f"河流有：{river.title()}.")

print("-----------------------------------------")
print("-----------------------------------------")

# 练习6-6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
new_names = ['edward', 'bob', 'phil', 'matt', 'danielle']
for name in new_names:
    if name in favorite_languages.keys():
        print(f"{name.title()},感谢你的参加！")
    else:
        print(f"{name.title()},希望你来参加！！")