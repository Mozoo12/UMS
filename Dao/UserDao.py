import pymysql
from Model.User import User


class UserDao:
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            user="admin2008",
            password="admin&&20081212",
            port=3306,
            database="mzvideo"
        )
        self.cursor = self.conn.cursor()

    def get_all_user(self):
        user_list = []
        self.conn.ping(reconnect=True)
        self.cursor.execute("select * from user;")
        for i in self.cursor.fetchall():
            user_list.append(User(i[0], i[1], i[2], i[3], i[4]))
        return user_list

    def get_user_by_username(self, username):
        self.conn.ping(reconnect=True)
        self.cursor.execute(f"select * from user where username='{username}';")
        for i in self.cursor.fetchall():
            return User(i[0], i[1], i[2], i[3], i[4])

    def get_user_by_keyword(self, keyword):
        user_list = []
        self.conn.ping(reconnect=True)
        self.cursor.execute(f"select * from user where username like '%{keyword}%' or password like '%{keyword}%';")
        for i in self.cursor.fetchall():
            print(i)
            user_list.append(User(i[0], i[1], i[2], i[3], i[4]))
        return user_list

    def add_user(self, username, password, token):
        self.conn.ping(reconnect=True)
        self.cursor.execute(f"insert into user (username,password,role,token) values "
                            f"('{username}','{password}','user','{token}')")
        self.conn.commit()

    def del_user_by_uid(self, uid: int):
        self.conn.ping(reconnect=True)
        self.cursor.execute(f"delete from user where uid='{uid}'")
        self.conn.commit()

    def update_user_by_uid(self, uid: int, username, password, role):
        self.conn.ping(reconnect=True)
        self.cursor.execute(f"update user set username='{username}', password='{password}', role='{role}' \
        where uid={uid}")
        self.conn.commit()

    def update_user_token(self, uid: int, token):
        self.conn.ping(reconnect=True)
        self.cursor.execute(f"update user set token='{token}' where uid='{uid}'")
        self.conn.commit()
