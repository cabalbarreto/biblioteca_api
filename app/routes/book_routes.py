from flask import Blueprint, jsonify, request, render_template
from app import app, db
from app.controllers.book_controller import BookController
from app.controllers.author_controller import AuthorController
from app.models import Author, Book

book_bp = Blueprint('book_bp', __name__, url_prefix='/api/books')

@app.route('/')
def home():
    """Rota para a interface web."""
    books = BookController.get_all_books()
    authors = AuthorController.get_all_authors()
    return render_template('index.html', books=books, authors=authors)

@app.route('/api/books', methods=['GET'])
def list_books():
    books = BookController.get_all_books()
    return jsonify([book.to_dict() for book in books])

@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = BookController.get_book_by_id(book_id)
    if book:
        return jsonify(book.to_dict())
    return jsonify({"message": "Livro não encontrado"}), 404

@app.route('/api/books', methods=['POST'])
def add_book():
    data = request.get_json()
    if not data or 'title' not in data or 'author_id' not in data:
        return jsonify({"message": "Dados inválidos"}), 400
    book = BookController.create_book(
        title=data['title'],
        publication_year=data.get('publication_year'),
        author_id=data['author_id']
    )
    if book:
        return jsonify(book.to_dict()), 201
    return jsonify({"message": "Autor não encontrado"}), 404

@app.route('/api/books/<int:book_id>', methods=['PUT'])
def edit_book(book_id):
    data = request.get_json()
    book = BookController.update_book(
        book_id=book_id,
        title=data.get('title'),
        publication_year=data.get('publication_year'),
        author_id=data.get('author_id')
    )
    if book:
        return jsonify(book.to_dict())
    return jsonify({"message": "Livro não encontrado"}), 404

@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def remove_book(book_id):
    success = BookController.delete_book(book_id)
    if success:
        return jsonify({"message": "Livro removido com sucesso"}), 200
    return jsonify({"message": "Livro não encontrado"}), 404