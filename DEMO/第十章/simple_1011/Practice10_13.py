import json


def get_stored_username():
    """如果存储了用户名，就获取它。(读)"""
    filename = 'username.json'
    try:
        with open(filename, 'r') as f:
            username = json.load(f)
    except FileNotFoundError:
        None
    else:
        return username


def get_new_username():
    """提示用户输入用户名。"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """问候用户，并指出其名字。"""
    username = get_stored_username()
    if username:
        answer = input(f"Are you {username}?")
        if answer == 'yes':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()

