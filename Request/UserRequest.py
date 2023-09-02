from pydantic import BaseModel
import typing


class Register(BaseModel):
    username: typing.Union[str, int]
    password: typing.Union[str, int]


class Login(BaseModel):
    username: typing.Union[str, int]
    password: typing.Union[str, int]
    remember: bool


class UpdateUserByUid(BaseModel):
    uid: int
    username: typing.Union[str, int]
    password: typing.Union[str, int]
    role: str
