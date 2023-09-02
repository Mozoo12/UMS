class User:
    def __init__(self, uid, username, password, role, token):
        # 用户ID
        self.uid = uid
        # 用户名
        self.username = username
        # 密码
        self.password = password
        # 用户角色，有admin, user两种
        self.role = role
        # 用户token值，有20位，登录时进行检测
        self.token = token

