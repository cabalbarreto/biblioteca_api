from app import db
from app.models import Loan, Book
from datetime import datetime

class LoanController:
    @staticmethod
    def get_all_loans():
        return Loan.query.all()

    @staticmethod
    def create_loan(book_id, borrower_name):
        book = Book.query.get(book_id)
        if not book:
            return None
        new_loan = Loan(book_id=book_id, borrower_name=borrower_name, loan_date=datetime.utcnow())
        db.session.add(new_loan)
        db.session.commit()
        return new_loan

    @staticmethod
    def update_loan(loan_id, return_date=None):
        loan = Loan.query.get(loan_id)
        if not loan:
            return None
        if return_date:
            loan.return_date = datetime.fromisoformat(return_date)
        db.session.commit()
        return loan

    @staticmethod
    def delete_loan(loan_id):
        loan = Loan.query.get(loan_id)
        if not loan:
            return False
        db.session.delete(loan)
        db.session.commit()
        return True
