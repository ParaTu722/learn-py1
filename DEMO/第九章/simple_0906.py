from random import randint, choice


# 练习9-13：骰子
class Die:
    """一个骰子"""
    def __init__(self, sides=6):
        """骰子的属性"""
        self.sides = sides

    def roll_die_6(self):
        """摇骰子"""
        return randint(1, 6)    # 要善于运用函数的返回值

    def roll_die_10(self):
        """摇骰子"""
        return randint(1, 10)


die6 = Die()
print(f"骰子最开始是:{die6.sides}")
print(f"六面骰子摇十次:")
for i in range(1, 11):
    print(f"\t{die6.roll_die_6()}")

print('\n------------------------------\n')

die10 = Die()
results = []
print(f"骰子最开始是:{die10.sides}")
for i in range(1, 11):
    result = die10.roll_die_10()
    results.append(result)
print(f"十面骰子摇十次:")
print(results)

print('\n------------------------------\n')

# 练习9-14：彩票

# 自己写的
"""
lottery_pond = [16, 'ttt', 1, 88, 'art', 77, 'pop', 147, 'qwer', 951, 36, 5]
lottery_items = []
for someone in range(1, 5):
    someone = choice(lottery_pond)
    lottery_items.append(someone)
print((f"中奖的四个是:{lottery_items}"))
"""

# 答案写的,运用更多，思路更好
possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = []

while len(winning_ticket) < 4:
    add_item = choice(possibilities)
    if add_item not in winning_ticket:
        winning_ticket.append(add_item)

print(f" We pulled a {winning_ticket}!")


print('\n------------------------------\n')
print('\n------------------------------\n')

# 练习 9-15 彩票分析


def show_winning_ticket(possibilities):
    """摇出中奖组合。"""
    winning_ticket = []
    while len(winning_ticket) < 4:
        add_item = choice(possibilities)
        if add_item not in winning_ticket:
            winning_ticket.append(add_item)
    return winning_ticket


def make_random_ticket(possibilities):
    """随机地生成彩票。"""
    ticket = []
    while len(ticket) < 4:
        add_item = choice(possibilities)
        if add_item not in ticket:
            ticket.append(add_item)
    return ticket


def check_ticket(played_tickets, winning_ticket):
    """检查彩票的每个数字或字母，只要有一个不在中奖组合中，就返回 False。"""
    for played_ticket in played_tickets:
        if played_ticket not in winning_ticket:
            # 没中奖，从此退出
            return False
    # 如果代码执行到这里，就说明中奖了！
    return True


new_possibilities = [1, 2, 3, 4, 5, 6, 7, 8,
                     9, 10, 'a', 'b', 'c', 'd', 'e']
win = show_winning_ticket(new_possibilities)
plays = 0
success = False
# 为避免程序执行时间太长，设置最多随机生成多少张彩票。
max_tries = 2_000_000

while not success:
    my_ticket = make_random_ticket(possibilities)
    success = check_ticket(my_ticket, win)
    plays += 1
    if plays >= max_tries:
        break

    if success:     # 等价于success为Ture
        print(f"Your ticket: {my_ticket}")
        print(f"Winning ticket: {win}\n")
        print(f"\tIt only took {plays} tries to win!\n")