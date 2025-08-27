from app import db
from app.models import Author

class AuthorController:
    @staticmethod
    def get_all_authors():
        return Author.query.all()

    @staticmethod
    def get_author_by_id(author_id):
        return Author.query.get(author_id)

    @staticmethod
    def create_author(name):
        new_author = Author(name=name)
        db.session.add(new_author)
        db.session.commit()
        return new_author
        
    @staticmethod
    def update_author(author_id, name):
        author = Author.query.get(author_id)
        if not author:
            return None
        author.name = name
        db.session.commit()
        return author

    @staticmethod
    def delete_author(author_id):
        author = Author.query.get(author_id)
        if not author:
            return False
        db.session.delete(author)
        db.session.commit()
        return True
