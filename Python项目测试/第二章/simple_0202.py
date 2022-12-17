# 变量字符串首字母大写，全大写，全小写
name ="ada lover"
print(name.title())
print(name.upper())
print(name.lower())

print("------------------------")

# 合并，拼接字符
first_name ="bob"
last_name ="seven"
full_name01 =f"{first_name}{last_name}"
full_name02 =f"{first_name} {last_name}"
print(full_name01)
print(full_name02)
print("------------------------")
print(f"Hello,{full_name02}!")
print(f"Hello, {full_name02}!")
print(f"Hello,{full_name02.title()}!")

print("------------------------")
message =f"Hello,{full_name02.title()}!"
print(message)

print("------------------------")
test_name ="eric"
test_word ="would you like to learn python"
print(f"Hi {test_name.title()},{test_word.lower()}?")
print(test_name.upper())
print(test_name.lower())
print(test_name.title())
