from flask import Blueprint, jsonify, request
from app import app
from app.controllers.loan_controller import LoanController

loan_bp = Blueprint('loan_bp', __name__, url_prefix='/api/loans')

@app.route('/api/loans', methods=['GET'])
def list_loans():
    loans = LoanController.get_all_loans()
    return jsonify([l.to_dict() for l in loans])

@app.route('/api/loans', methods=['POST'])
def add_loan():
    data = request.get_json()
    if not data or 'book_id' not in data or 'borrower_name' not in data:
        return jsonify({"message": "Dados inválidos"}), 400
    loan = LoanController.create_loan(data['book_id'], data['borrower_name'])
    if loan:
        return jsonify(loan.to_dict()), 201
    return jsonify({"message": "Livro não encontrado"}), 404

@app.route('/api/loans/<int:loan_id>', methods=['PUT'])
def edit_loan(loan_id):
    data = request.get_json()
    loan = LoanController.update_loan(loan_id, return_date=data.get('return_date'))
    if loan:
        return jsonify(loan.to_dict())
    return jsonify({"message": "Empréstimo não encontrado"}), 404

@app.route('/api/loans/<int:loan_id>', methods=['DELETE'])
def remove_loan(loan_id):
    success = LoanController.delete_loan(loan_id)
    if success:
        return jsonify({"message": "Empréstimo removido com sucesso"}), 200
    return jsonify({"message": "Empréstimo não encontrado"}), 404
