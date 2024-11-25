from flask import Flask, jsonify, request
from datos_dummy import books

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>My second API</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

# 1.Ruta para obtener todos los libros
@app.route('/v0/books', methods=['GET'])
def all_books():
    return books
    
# 2.Ruta para obtener un libro concreto mediante su id como parámetro en la llamada
@app.route('/v0/book_id', methods=['GET'])
def book_id():
    id = int(request.args['id'])
    results = [book for book in books if book["id"]==id]
    return results


# 3.Ruta para obtener un libro concreto mediante su título como parámetro en la llamada de otra forma
@app.route('/v0/book/<string:title>', methods=["GET"])
def book_title(title):
    results = [book for book in books if book["title"].lower()==title.lower()]
    return results


# 4.Ruta para obtener un libro concreto mediante su titulo dentro del cuerpo de la llamada  
@app.route('/v1/book', methods=["GET"])
def book_title_body():
    title = request.get_json().get('title', None)
    if not title:
        return "Not a valid title in the request", 400
    else:
        results = [book for book in books if book["title"].lower()==title.lower()]
        if results == []:
            return "Book not found", 400
        else:
            return results

# 5.Ruta para añadir un libro mediante un json en la llamada
@app.route('/v1/add_book', methods=["POST"])
def post_books():
    data = request.get_json()
    books.append(data)
    return books


# 6.Ruta para añadir un libro mediante parámetros
@app.route('/v2/add_book', methods=["POST"])
def post_books_v2():
    book = {}
    book['id'] = int(request.args['id'])
    book['title'] = request.args['title']
    book['author'] = request.args['author']
    book['first_sentence'] = request.args['first_sentence']
    book['published'] = request.args['published']
    books.append(book)
    return books

# 7.Ruta para modificar un libro
@app.route("/v3/books", methods=["PUT"])
def put_book():
    id = int(request.args['id'])

    title = request.args.get('title', None)
    author = request.args.get('author', None)

    for book in books:
        if book["id"] == id:
            if title:
                book['title'] = title
            if author:
                book['author'] = author
    return books

# 8.Ruta para eliminar un libro
@app.route("/v4/books", methods=["DELETE"])
def del_book():
    id = int(request.args['id'])
    # id = int(id)
    for book in books:
        if book["id"] == id:
            books.remove(book)
    return books

app.run()