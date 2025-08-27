from app import db
from datetime import datetime

class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    books = db.relationship('Book', backref='author', lazy=True, cascade="all, delete-orphan")
    
    def to_dict(self):
        return {"id": self.id, "name": self.name}

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    publication_year = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    loans = db.relationship('Loan', backref='book', lazy=True, cascade="all, delete-orphan")
    
    def to_dict(self):
        return {
            "id": self.id, 
            "title": self.title, 
            "publication_year": self.publication_year,
            "author_name": self.author.name
        }

class Loan(db.Model):
    __tablename__ = 'loans'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    borrower_name = db.Column(db.String(128), nullable=False)
    loan_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    return_date = db.Column(db.DateTime)
    
    def to_dict(self):
        return {
            "id": self.id, 
            "book_title": self.book.title,
            "borrower_name": self.borrower_name,
            "loan_date": self.loan_date.isoformat(),
            "return_date": self.return_date.isoformat() if self.return_date else None
        }
