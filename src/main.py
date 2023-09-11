from typing import Union
import json
import uvicorn
import os

from fastapi import FastAPI, Request

app = FastAPI()
port = os.getenv('PORT', 3000)
if type(port) == str:
  port = int(port)

@app.get("/")
def read_root(request: Request):
  client = json.dumps(request.client)
  return {"message": "Hello World", 'client': json.loads(client) }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
  return {"item_id": item_id, "q": q}

if __name__ == '__main__':
  uvicorn.run(app, host="0.0.0.0", port=port)
