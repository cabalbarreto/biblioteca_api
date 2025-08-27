from app import db
from app.models import Book, Author

class BookController:
    @staticmethod
    def get_all_books():
        return Book.query.all()

    @staticmethod
    def get_book_by_id(book_id):
        return Book.query.get(book_id)

    @staticmethod
    def create_book(title, publication_year, author_id):
        author = Author.query.get(author_id)
        if not author:
            return None
        new_book = Book(title=title, publication_year=publication_year, author_id=author_id)
        db.session.add(new_book)
        db.session.commit()
        return new_book

    @staticmethod
    def update_book(book_id, title=None, publication_year=None, author_id=None):
        book = Book.query.get(book_id)
        if not book:
            return None
        if title:
            book.title = title
        if publication_year:
            book.publication_year = publication_year
        if author_id:
            book.author_id = author_id
        db.session.commit()
        return book

    @staticmethod
    def delete_book(book_id):
        book = Book.query.get(book_id)
        if not book:
            return False
        db.session.delete(book)
        db.session.commit()
        return True