from fastapi import FastAPI, requests, HTTPException
from pydantic import BaseModel
import sqlite3
import uvicorn

app = FastAPI()

class Book(BaseModel):
    published: int
    author: str
    title: str
    first_sentence: str


conn = sqlite3.connect('books.db')
cursor = conn.cursor()

@app.get("/")
async def hello():
    return "Hello world"

# 0.Ruta para obtener todos los libros
@app.get("/books")
async def get_books():
    cursor.execute("SELECT * FROM books")
    results = cursor.fetchall()
    return dict({"results":results})

# 1.Ruta para obtener el conteo de libros por autor ordenados de forma descendente
@app.get("/books/authorcount")
async def get_books_byauthor():
    cursor.execute("""
                    SELECT
                        author,
                        COUNT(title)
                    FROM books
                    GROUP BY 1
                    ORDER BY 2 DESC
                   """)
    results = cursor.fetchall()
    return dict(results)


# 2.Ruta para obtener los libros de un autor
@app.get("/authors/books")
async def get_books_by_author(author: str):
    cursor.execute("SELECT * FROM books WHERE author LIKE ?", (f"%{author}%",))
    results = cursor.fetchall()
    if not results:
        raise HTTPException(status_code=404, detail=f"No books found for author {author}")
    return dict({"results":results})


@app.get("/authors/{author}/books")
async def get_books_by_author(author: str):
    cursor.execute("SELECT * FROM books WHERE author LIKE ?", (f"%{author}%",))
    results = cursor.fetchall()
    if not results:
        raise HTTPException(status_code=404, detail=f"No books found for author {author}")
    return dict({"results":results})


# 3.Ruta para añadir un libro
@app.post("/books")
async def create_book(book:Book):
    try:
        cursor.execute(
            """
                INSERT INTO books (published, author, title, first_sentence)
                VALUES (?, ?, ?, ?)
            """,
            (book.published, book.author, book.title, book.first_sentence)
        )
        conn.commit()
        return {"message": f"Book {book.title} added successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error inserting book: " + str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)