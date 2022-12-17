# 练习6-1
infomations = {}
infomations['first_name'] = '张'
infomations['last_name'] = '三'
infomations['age'] = '28'
infomations['city'] = '北京'
print(infomations)

print('--------------------------------------------')
print('--------------------------------------------')

# 练习6-2
numbers = {}
numbers['bob'] = 2
numbers['tom'] = 56
numbers['jim'] = 900_000
numbers['ming'] = 84

num = numbers['jim']
print(f"Mandy's favorite number is {num}.")
#以此类推

print('--------------------------------------------')
print('--------------------------------------------')

# 练习6-3
glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs."
    }
word = 'string'
print(f"{word.title()}: {glossary[word]}")
word = 'comment'
print(f"{word.title()}: {glossary[word]}")
word = 'list'
print(f"{word.title()}: {glossary[word]}")