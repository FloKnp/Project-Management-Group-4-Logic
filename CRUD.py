from fastapi import FastAPI, HTTPException
#from pydantic import BaseModel
import mysql.connector
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="testdb"
    )

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic Model
# class Item(BaseModel):
#     name: str
#     description: str

# Create Item
@app.post("/items/")
def create_item(item):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO items (name, description) VALUES (%s, %s)", (item.name, item.description))
    db.commit()
    cursor.close()
    db.close()
    return {"message": "Item created successfully"}

# Read Items
@app.get("/items/")
def read_items():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    cursor.close()
    db.close()
    return items

# Read Item by ID
@app.get("/items/{item_id}")
def read_item(item_id: int):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items WHERE id = %s", (item_id,))
    item = cursor.fetchone()
    cursor.close()
    db.close()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# Delete Item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("DELETE FROM items WHERE id = %s", (item_id,))
    db.commit()
    cursor.close()
    db.close()
    return {"message": "Item deleted successfully"}

# verify answer
@app.post("/verify/")
def verify(user_input: str, question_ID: int):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT answer FROM items WHERE ques_id = %s", (question_ID,))
    ans = cursor.fetchone()

    cursor.close()
    db.close()

    if (ans == user_input):
        return {"message" : "correct answer"}
    else:
        return {"message" : "wrong answer",
                "correct answer": ans}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)



    
