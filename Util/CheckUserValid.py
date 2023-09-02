import random


def check_legality(username, password):
    """检查登陆注册时用户输入是否合法"""
    if "-" in username or " " in username or "/" in username or "*" in list(username) or \
            "-" in password or " " in password or "/" in password or "*" in list(password):
        return False
    else:
        return True


def create_token():
    str_list = ["A", "c", "H", "O", "$", "#", "@", "K", "B"]
    token = ""
    for i in range(0, 20):
        token += random.choice(str_list)
    return token

