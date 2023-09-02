from fastapi import FastAPI, Request
import uvicorn
import Controller.UserController as user

app = FastAPI()

app.include_router(user.userAPI)


@app.middleware("http")
async def middle(request: Request, call_next):
    response = await call_next(request)
    if request.cookies.get("token"):
        return response


if __name__ == "__main__":
    uvicorn.run(app, port=8080)
