# 测试函数

def get_formatted_name(first, last, middle=''):
    """"make all name """
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()