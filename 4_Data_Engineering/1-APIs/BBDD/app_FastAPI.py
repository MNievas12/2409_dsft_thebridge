from fastapi import FastAPI, HTTPException
from datos_dummy import books
import uvicorn



app = FastAPI()

@app.get('/')
async def home():
    return "Bienvenido a la API de la base de datos de libros"

# Ruta para obtener todos los libros
@app.get("/v1/books")
async def get_all_books():
    return books

# Ruta para obtener información de un libro por su id
@app.get("/v1/books/{book_id}")
async def get_book_by_id(book_id: int):
    results = [book for book in books if book["id"] == book_id]
    if not results:
        raise HTTPException(status_code=404, detail="Book not found")
    return results

# Endpoint para añadir un libro
@app.post("/v1/books", status_code=201)
async def add_book(title: str, author: str, year: int):
    new_book = {"title": title, "author": author, "year": year}
    books.append(new_book)
    return new_book

# Endpoint para modificar un libro por su índice
@app.put("/v1/books/{index}")
async def update_book(index: int, title: str, author: str, year: int):
    if index < 0 or index >= len(books):
        raise HTTPException(status_code=404, detail="Book not found")
    books[index] = {"title": title, "author": author, "year": year}
    return books[index]

# Endpoint para eliminar un libro por su índice
@app.delete("/v1/books/{index}")
async def delete_book(index: int):
    if index < 0 or index >= len(books):
        raise HTTPException(status_code=404, detail="Book not found")
    deleted_book = books.pop(index)
    return deleted_book



# Ejecutar la aplicación
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)