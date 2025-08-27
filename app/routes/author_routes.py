from flask import Blueprint, jsonify, request
from app import app
from app.controllers.author_controller import AuthorController

author_bp = Blueprint('author_bp', __name__, url_prefix='/api/authors')

@app.route('/api/authors', methods=['GET'])
def list_authors():
    authors = AuthorController.get_all_authors()
    return jsonify([a.to_dict() for a in authors])

@app.route('/api/authors/<int:author_id>', methods=['GET'])
def get_author(author_id):
    author = AuthorController.get_author_by_id(author_id)
    if author:
        return jsonify(author.to_dict())
    return jsonify({"message": "Autor não encontrado"}), 404

@app.route('/api/authors', methods=['POST'])
def add_author():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"message": "Dados inválidos"}), 400
    author = AuthorController.create_author(name=data['name'])
    return jsonify(author.to_dict()), 201

@app.route('/api/authors/<int:author_id>', methods=['PUT'])
def edit_author(author_id):
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"message": "Dados inválidos"}), 400
    author = AuthorController.update_author(author_id, data['name'])
    if author:
        return jsonify(author.to_dict())
    return jsonify({"message": "Autor não encontrado"}), 404

@app.route('/api/authors/<int:author_id>', methods=['DELETE'])
def remove_author(author_id):
    success = AuthorController.delete_author(author_id)
    if success:
        return jsonify({"message": "Autor removido com sucesso"}), 200
    return jsonify({"message": "Autor não encontrado"}), 404
