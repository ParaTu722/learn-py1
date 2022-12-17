# 练习4-3,　使用一个for 循环打印数1～20
number = [value for value in range(1,21)]
print(number)

numbers = list(range(1, 21))
print(numbers)

'''
for value in range(1, 21):
    print(value) 
'''

# 练习4-4,4-5
new_numbers = list(range(1, 1_000_001))
# print(new_numbers)
print(f"sum is:{sum(new_numbers)}")
print("---------------------------------")

# 练习4-6
#jishus = list(range(1, 21, 2))
for jishu in list(range(1, 21, 2)):
    print(jishu)
print("---------------------------------")

# 练习4-7
beishus = []
for beishu in list(range(3, 31,3)):
    beishus.append(beishu)
print(beishus)
print("---------------------------------")

# 练习4-8,!!!!!!!!!!
lifangs = list(range(1, 11))
for value in lifangs:
    values = value**3   # 搞清楚不同变量的调用，定义
    print(values)
print("---------------------------------")

# 练习4-9
last_lifang = [value**3 for value in range(1, 11)]
print(last_lifang)