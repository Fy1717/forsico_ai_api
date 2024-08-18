from app.models import db
from app import createApp
import os
# import psycopg2
# from psycopg2 import sql
# from app.models import Log

# Migration işlemleri için dosya dizininde yapılması gereken terminal kodları
# flask db init
# flask db migrate -m "initial commit"
# flask db upgrade


SECRET_KEY = os.getenv('SECRET_KEY', 'Bnxfm3x42ynnTUONOuE7gXCmb2oXYFzL')

# Çevre değişkenlerinden veritabanı bilgilerini al
DB_USERNAME = os.getenv('DB_USERNAME', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'forsico_io_ai')
DB_PORT = os.getenv('DB_PORT', 5001)


def createDB():
    app = createApp()
    with app.app_context():
        # check_and_create_database()
        db.create_all()
