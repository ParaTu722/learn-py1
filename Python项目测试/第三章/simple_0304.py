# 根据值删除元素,可使用方法remove()
# 方法remove()只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来判断是否删除了所有这样的值
fruit = ['apple', 'pear', 'banana', 'watermelon']
print(fruit)
fruit.remove('pear')
print(fruit)
print("------------------------------")
other_fruit = 'banana'
fruit.remove(other_fruit)
print(fruit)

print(f"我最后吃了{other_fruit.title()}!")
print("------------------------------")
print("------------------------------")
print("------------------------------")

# 练习
guest = ['张三', '李四', '王五', '赵六']
print(f"今晚宴会的嘉宾有：{guest}！非常欢迎你们来参加！！！")

print(f"今晚《{guest[1]}》有事来不了了，很遗憾。")
guest[1]='钱七'
print(f"\t诚挚邀请：{guest[0]}来赴宴！")
print(f"\t诚挚邀请：{guest[1]}来赴宴！")
print(f"\t诚挚邀请：{guest[2]}来赴宴！")
print(f"\t诚挚邀请：{guest[3]}来赴宴！")

# 更多的人参加
guest.insert(0, '马二')
guest.insert(3, '孙十')
guest.append('郑九')
print(f"最后今晚宴会的嘉宾有：{guest}！非常欢迎你们来参加！！！")

# 人员缩减
print(f"可是只有{guest[2]},{guest[4]}能来参加。")
poped_guest = guest.pop()
print(f"sorry!{poped_guest} you out")
poped_guest = guest.pop()
print(f"sorry!{poped_guest} you out")
poped_guest = guest.pop(3)
print(f"sorry!{poped_guest} you out")
poped_guest = guest.pop(1)
print(f"sorry!{poped_guest} you out")
poped_guest = guest.pop(0)
print(f"sorry!{poped_guest} you out")
print(f"\tcongratulations：{guest[0]},你还在！")
print(f"\tcongratulations：{guest[1]},你还在！")
print(f"我邀请了 {len(guest)} 位嘉宾！！！")

'''
# 确保列表为空
del guest[0]
del guest[1]
print(f"看看最后还有：{guest}  ！")
'''

