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


# Endpoint para modificar un libro por su índice


# Endpoint para eliminar un libro por su índice

# Ejecutar la aplicación
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)