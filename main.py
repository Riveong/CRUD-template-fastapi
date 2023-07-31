from fastapi import FastAPI

data = {
    1:{"something":"a"},
    2:{"something":"b"},
    3:{"something":"c"},
}



app = FastAPI()

@app.get("/")
def getItems():
    return data


@app.get("/{id}")
def getItem(id:int):
    return data[id]

@app.post("/")
def addItem(something):
    newId = len(data.keys()) + 1
    data[newId] = {"something":something}
    return data


@app.put("/{id}")
def updateItem(id:int, somethinga):
    data[id]['something'] = somethinga
    return data


@app.delete("/{id}")
def deleteItem(id:int):
    del data[id]
    return data


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=port, timeout_keep_alive=1200)