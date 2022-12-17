# 8.4 传递列表
def greet_user(names):
    """向列表中的每位用户发出简单的问候。"""
    for name in names:
        msg = f"\tHello, {name.title()}!"
        print(msg)
userlist = ['hannah', 'ty', 'margot']
greet_user(userlist)
"""
将greet_users() 定义为接受一个名字列表，并将其赋给形参names。这个
函数遍历收到的列表，并对其中的每位用户打印一条问候语
"""
print('----------------------------------------------')
print('----------------------------------------------')
print('----------------------------------------------')
# 8.4.1 在函数中修改列表
"""
# 不使用函数：
# 首先创建一个列表，其中包含一些要打印的设计。
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
# 模拟打印每个设计，直到没有未打印的设计为止。
# 打印每个设计后，都将其移到列表completed_models中。
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
# 显示打印好的所有模型。
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
"""
def print_models(unprinted_designs, completed_models):
    """模拟打印每个设计，直到没有未打印的设计为止。打印每个设计后，都将其移到列表completed_models中"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型。"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(f"\t{completed_model}")
'''
  创建了一个未打印的设计列表，还创建了一个空列表，用于存储打印好的模型。
接下来，由于已经定义了两个函数，只需调用它们并传入正确的实参即可。
'''
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)   # print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

# 8.4.2 禁止函数修改列表
# function_name(list_name_[:])>>>>>>>>>函数名(列表名[:])      见52行

print('----------------------------------------------')
print('----------------------------------------------')
# 动手试一试
# 练习8-9：消息
def show_messages(print_lists):
    """打印列表中的每条文本消息"""
    print("Showing all messages:")
    for print_list in print_lists:
        print(f"\t你输入的消息是:{print_list.title()}")

def send_messages(print_lists, sent_messages):
    """将每条消息都打印出来,并移到sent_messages()"""
    print("\nSending all messages:")
    while print_lists:      # 用for会出错 for print_list in  print_lists:
        new_print_list = print_lists.pop()
        print(f"\t转移后的消息是：{new_print_list}")
        sent_messages.append(new_print_list)


new_list = ['gfhsjujsa', 'sdgfjsgf7uw', 'iuyuywoo654']
show_messages(new_list)

new_null_list = []
send_messages(new_list, new_null_list)      # send_messages(new_list[:], new_null_list)

# 练习 8-11 消息归档 81行
