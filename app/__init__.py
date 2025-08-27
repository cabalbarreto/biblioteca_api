from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app.routes import book_routes, author_routes, loan_routes

app.register_blueprint(book_routes.book_bp)
app.register_blueprint(author_routes.author_bp)
app.register_blueprint(loan_routes.loan_bp)

from app import models