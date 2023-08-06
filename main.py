from fastapi import FastAPI

todos = [
    {
        "id": "1",
        "item": "Commit crimes."
    },
    {
        "id": "2",
        "item": "Meet Ryan renolds' mom."
    },
        {
        "id": "3",
        "item": "Make fun of genshiners."
    }
]

data = "what"

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app = FastAPI()

@app.get("/")
def getItems():
    return data

@app.get("/todo", tags=["todos"])
async def get_todos():
    return { "data": todos }

@app.post("/todo", tags=["todos"])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return {
        "data": { "Todo added." }
    }


@app.put("/todo/{id}", tags=["todos"])
async def update_todo(id: int, body: dict) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todo["item"] = body["item"]
            return {
                "data": f"Todo with id {id} has been updated."
            }

    return {
        "data": f"Todo with id {id} not found."
    }


@app.delete("/todo/{id}", tags=["todos"])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todos.remove(todo)
            return {
                "data": f"Todo with id {id} has been removed."
            }

    return {
        "data": f"Todo with id {id} not found."
    }


if __name__ == '__main__':
     uvicorn.run("app.api:app", host="0.0.0.0", port=port, reload=True)
