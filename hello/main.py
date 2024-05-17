from fastapi import FastAPI
import uvicorn

app=FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello World!"}

@app.get("/gettodos")
def getTodos():
    print ("Get Todos called")
    return "Get Todos called"

@app.get("/getSingleTodo")
def getSingleTodo():
    print("Get Todo called")
    return "GetSingleTodos called"

@app.post("/getposttodo")
def getTodoPost():
    print("Get Todo called")
    return "getPostTodo called"

@app.put("/getputtodo")
def getputtodo():
    print("Put Todo called")
    return "getPutTodo called"

@app.delete("/getdeletetodo")
def getTododelete():
    print("Get Todo called")
    return "getDeleteTodo called"

def start():
    uvicorn.run("hello.main:app",host="127.0.0.1",port=8080,reload=True)