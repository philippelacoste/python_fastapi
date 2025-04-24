from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    with open("./data/sample_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    print(data["tickets"][0])
    found = filter(lambda x: x["id"]== item_id.__str__(),data["tickets"])
    return list(found)

import json
import uvicorn

if __name__ == "__main__":
    # with open("./config/config.json", "r", encoding="utf-8") as f:
    #     config = json.load(f)
    uvicorn.run("main:app")