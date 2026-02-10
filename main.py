
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, quantity: str | None = None) -> dict[int | None ]:
    return {"item_id": item_id, "quantity": quantity}
