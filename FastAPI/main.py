from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Book(BaseModel):
    id: int
    name: str
    price: float
    is_offer: bool = None

books: List[Book] = [Book(id=1, name="Book 1", price=10.99, is_offer=True)]

# these are decorators that define the routes for the API
@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Store!"}

@app.get("/books")
def read_books():
    return books

@app.post("/books")
def add_book(book: Book):
    books.append(book)
    return book

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books):
        if book.id == book_id:
            books[index] = updated_book
            return updated_book
    return {"error": "Book not found"}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            delete = books.pop(index)
            return delete
    return {"error": "Book not found"}
