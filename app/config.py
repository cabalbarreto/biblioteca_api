
import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'geleira@1')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', "postgresql://postgres:SECRET_KEY@127.0.0.1:5433/biblioteca_api_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False