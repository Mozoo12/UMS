from fastapi import APIRouter, Response, Request
import Request.UserRequest as req
from Service.UserService import UserService

userAPI = APIRouter()

service = UserService()


@userAPI.get("/getuserbykw/{keyword}")
def get_user_by_kw(keyword: str):
    return service.get_user_by_keyword(keyword=keyword)


@userAPI.get("/getalluser")
def get_all_user():
    return service.get_all_user()


@userAPI.delete("/deluserbyuid/{uid}")
def del_user_by_uid(uid: int):
    service.del_user_by_uid(uid)
    return {"msg": "用户删除成功"}


@userAPI.put("/updateuserbyuid")
def update_user_by_uid(request: req.UpdateUserByUid):
    service.update_user_by_uid(
        uid=request.uid,
        username=request.username,
        password=request.password,
        role=request.role
    )
    return {"msg": "用户信息更新成功"}


@userAPI.post("/login")
def login(request: req.Login, response: Response):
    result = service.login(
        username=request.username,
        password=request.password
    )
    if result.get("state") == 0:
        return {"msg": "输入包含非法字符", "islogin": False}
    elif result.get("state") == -1:
        return {"msg": "用户名错误", "islogin": False}
    elif result.get("state") == -2:
        return {"msg": "密码错误", "islogin": False}
    else:
        if request.remember:
            response.set_cookie("token", result.get("user").token)
        return {"msg": "登陆成功", "islogin": True, "user": result.get("user").token}


@userAPI.post("/register")
def register(request: req.Register):
    result = service.register(
        username=request.username,
        password=request.password
    )
    if result.get("state") == -1:
        return {"msg": "输入包含非法字符"}
    elif result.get("state") == 0:
        return {"msg": "用户名已存在"}
    else:
        return {"msg": "注册成功"}
