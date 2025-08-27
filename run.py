from app import app, db
from app.models import Author, Book, Loan
import os

with app.app_context():
    db.create_all()
    if not Author.query.first():
        db.session.add(Author(name='Linda Barreto'))
        db.session.commit()
    if not Book.query.first():
        author_id = Author.query.filter_by(name='Linda Barreto').first().id
        db.session.add(Book(title='Aula inaugural', publication_year=1999, author_id=author_id))
        db.session.commit()

from flask import render_template
@app.route('/')
def home_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)