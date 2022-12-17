# 练习7-8：熟食店
sandwich_orders = ['chicken', 'fish', 'beef', 'pastrami']
finished_sandwiches = []
while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print(f"I made your {sandwich_order.title()} sandwich")
    finished_sandwiches.append(sandwich_order)
print(f"所有三明治都已制作好:")
for finished_sandwiche in finished_sandwiches:
    print(f"\t{finished_sandwiche}")

print('---------------------------------------------------')
print('---------------------------------------------------')

# 练习7-9 五香烟熏牛肉卖完了
new_sandwich_orders = ['pastrami', 'chicken', 'pastrami', 'fish', 'beef', 'pastrami']
print("熟食店的五香烟熏牛肉(pastrami）卖完了")
while 'pastrami' in new_sandwich_orders:
    new_sandwich_orders.remove('pastrami')
print(f"现在有:{new_sandwich_orders}")

print('---------------------------------------------------')
print('---------------------------------------------------')

# 练习7-10：梦想的度假胜地
dream_places = {}
active = True
while active:
    name = input("What is your name?")
    places = input("\tIf you could visit one place in the world, where would you go?")
    dream_places[name] = places

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        active = False
print(f"经过调查：")
for key, value in dream_places.items():
    print(f"\t{key}最想去的地方是：{value}")