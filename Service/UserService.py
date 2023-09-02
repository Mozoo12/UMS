from Dao.UserDao import UserDao
import Util.CheckUserValid as cuv

dao = UserDao()


class UserService:
    @classmethod
    def get_all_user(cls):
        user = dao.get_all_user()
        if user is not None:
            return [i.__dict__ for i in dao.get_all_user()]
        return {"msg": "暂无用户"}

    @classmethod
    def get_user_by_keyword(cls, keyword):
        user = dao.get_user_by_keyword(keyword=keyword)
        if user is not None:
            return [i.__dict__ for i in dao.get_user_by_keyword(keyword=keyword)]
        return {"msg": "暂无匹配用户"}

    @classmethod
    def del_user_by_uid(cls, uid: int):
        dao.del_user_by_uid(uid=uid)

    @classmethod
    def update_user_by_uid(cls, uid: int, username, password, role):
        dao.update_user_by_uid(uid=uid, username=username, password=password, role=role)

    @classmethod
    def register(cls, username, password):
        if cuv.check_legality(username=username, password=password):
            if dao.get_user_by_username(username=username) is None:
                dao.add_user(username=username, password=password, token=cuv.create_token())
                return {"state": 1}
            else:
                return {"state": 0}
        else:
            return {"state": -1}

    @classmethod
    def login(cls, username, password):
        if cuv.check_legality(username=username, password=password):
            user = dao.get_user_by_username(username=username)
            if user is not None:
                if user.password == password:
                    dao.update_user_token(uid=user.uid, token=cuv.create_token())
                    return {"user": user, "state": 1}
                else:
                    return {"state": "-2"}
            else:
                return {"state": -1}
        else:
            return {"state": 0}
