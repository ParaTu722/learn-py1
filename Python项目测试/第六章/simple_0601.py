# 6.1 一个简单的字典
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'].upper())
print(alien_0['points'])
# 在该字典中，字符串'color' 是一个键，与之相关联的值为'green'
print('----------------------------------------------')
print('----------------------------------------------')

# 6.2.1 访问字典中的值
alien_0 = {'color': 'yellow', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")
# 先定义了一个字典。然后，从这个字典中获取与键'points' 相关联的值，并将这个值赋给变量new_points,接下来，将整数转换为字符串，并打印

# 6.2.2 添加键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print('----------------------------------------------')
print('----------------------------------------------')

# 6.2.3 先创建一个空字典
alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)

# 6.2.4 修改字典中的值
print(f"The alien is {alien_1['color'].title()}.")
alien_1['color'] = 'red'
print(f"The alien is now {alien_1['color'].title()}.")

print('----------------------------------------------')
print('----------------------------------------------')

# 能够以不同速度移动的外星人进行位置跟踪的例子
alien_2= {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_2['x_position']}")
alien_2['speed'] = 'fast'
# 向右移动外星人。
# 根据当前速度确定将外星人向右移动多远。
if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
# 新位置为旧位置加上移动距离
alien_2['x_position'] = alien_2['x_position'] + x_increment
print(f"New position: {alien_2['x_position']}")

'''
    首先定义一个外星人，其中包含初始 坐标和 坐标，还有速度'medium' 。出于
简化考虑，省略了颜色和分数，但即便包含这些键值对，本例的工作原理也不会有
任何变化。我们还打印了x_position 的初始值，旨在让用户知道这个外星人向右
移动了多远。
    使用一个if-elif-else 结构来确定外星人应向右移动多远，并将这个值赋给
变量x_increment 。如果外星人的速度为'slow' ，它将向右移动一个单位；如
果速度为'medium' ，将向右移动两个单位；如果为'fast' ，将向右移动三个单
位。确定移动距离后，将其与x_position 的当前值相加（，再将结果关联
到字典中的键x_position 。
'''

print('----------------------------------------------')
print('----------------------------------------------')

# 6.2.5 删除键值对
print(alien_0)
# 使用del语句时，必须指定字典名和要删除的键。
del alien_0['points']
print(alien_0)

print('----------------------------------------------')
print('----------------------------------------------')

#6.2.6 由类似对象组成的字典
favorite_languages = {
    'bob': 'c++',
    'jen': 'c',
    'phil': 'python',
    'edward': 'ruby',
    }
language = favorite_languages['phil'].title()
print(f"Phil's favorite language is {language}.")

print('----------------------------------------------')
print('----------------------------------------------')

# 6.2.7 使用get() 来访问值
print(alien_0)
# print(alien_0['points'])      报错，指出存在键值错误
# 方法get() 的第一个参数用于指定键，是必不可少的；第二个参数为指定的键不存在时要返回的值，是可选的
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
# 若字典中有键'points'，将获得与之相关联的值；若无，将获得指定的默认值。
# 虽然这里没有键'points' ，但将获得一条清晰的消息，不会引发错误
# 方法get() 与第十章相关