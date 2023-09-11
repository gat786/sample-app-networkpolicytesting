from typing import Union
import json

from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def read_root(request: Request):
  client = json.dumps(request.client)
  return {"message": "Hello World", 'client': json.loads(client) }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
  return {"item_id": item_id, "q": q}
