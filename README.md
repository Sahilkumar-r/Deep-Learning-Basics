<<<<<<< HEAD
# Simple FastAPI App

A minimal FastAPI application with a hello endpoint and basic in-memory CRUD for items.

## Requirements

- Python 3.9+

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload
```

The app runs at http://127.0.0.1:8000. Interactive API docs are at http://127.0.0.1:8000/docs.

## Endpoints

| Method | Path               | Description          |
|--------|--------------------|----------------------|
| GET    | `/`                | Hello message        |
| GET    | `/hello/{name}`    | Greet a name         |
| GET    | `/items`           | List all items       |
| GET    | `/items/{item_id}` | Get one item         |
| POST   | `/items`           | Create an item       |
| PUT    | `/items/{item_id}` | Update an item       |
| DELETE | `/items/{item_id}` | Delete an item       |

## Example

```bash
curl -X POST http://127.0.0.1:8000/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Notebook", "price": 4.99, "in_stock": true}'
```

## Notes

Items are stored in memory, so data is lost when the server restarts.
=======
# fastapi-basics
>>>>>>> 5d21eb75103692ac8697750314ee1d2924c1b125
