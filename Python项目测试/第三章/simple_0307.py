# 将第三章所学全部使用
# -------------------------------
citys = ['chongqin', 'shanxi', 'beijin', 'hebei', 'fujian']
print(f"首次打印列表：{citys}")
print(f"我最喜的城市是：{citys[1].title()}!!!")
print(f"我学习的城市是：{citys[-1].title()}!!!")
# 修改列表元素
citys[0] = 'xinjiang'
print(citys)
# 添加列表元素
citys.append('jiangsu')     # 在列表末尾添加元素
citys.insert(1, 'shanghai')     #可在列表的任何位置添加新元素
citys.insert(1, 'tianjin')
citys.insert(1, 'taiwan')
print(citys)
del citys[0]    #使用del 语句将值从列表中删除后，你就无法再访问它了
del citys[-2]
print(citys)

poped_city = citys.pop(1)    #方法pop() 删除列表末尾的元素，并让你能够接着使用它,()中为空则默认最后一个
print(citys)
print(poped_city)

empyt_city = 'shanghai'
citys.remove(empyt_city)    # 根据值删除元素
print(f"我又删除了{empyt_city}")

'''
# 使用方法sort() 对列表永久排序
citys.sort()
print(citys)
citys.sort(reverse=True)
print(citys)
'''

print(f"临时排个序：{sorted(citys)}")
print(f"再临时排个序：{sorted(citys, reverse=True)}")
citys.reverse()
print(f"我倒着显示:{citys}")
citys.reverse()
print(f"我再倒着显示:{citys}")
print(len(citys))

# 索引-1 总是返回最后一个列表元素,仅当列表为空时，这种访问最后一个元素的方式才会导致错误