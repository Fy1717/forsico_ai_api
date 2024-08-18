from app.models import db
from app import createApp
import os
import psycopg2
from psycopg2 import sql
from app.models import Log        

#Migration işlemleri için dosya dizininde yapılması gereken terminal kodları
#flask db init
#flask db migrate -m "initial commit"
#flask db upgrade


SECRET_KEY = "Bnxfm3x42ynnTUONOuE7gXCmb2oXYFzL"

# Çevre değişkenlerinden veritabanı bilgilerini al
DB_USERNAME = os.getenv('DB_USERNAME', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'forsico_io_ai')
DB_PORT = os.getenv('DB_PORT', 5001)

'''
def check_and_create_database():
    # Veritabanına bağlan
    conn = psycopg2.connect(
        dbname=DB_NAME,  # postgres varsayılan veritabanına bağlan
        user=DB_USERNAME,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    conn.autocommit = True  # Veritabanı değişikliklerini otomatik işle
    cur = conn.cursor()

    # Belirtilen veritabanının olup olmadığını kontrol et
    cur.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s", (DB_NAME,))
    exists = cur.fetchone()
    if not exists:
        # Veritabanı yoksa, yeni bir tane oluştur
        cur.execute(sql.SQL("CREATE DATABASE {}").format(
            sql.Identifier(DB_NAME)
        ))
        print(f"Database {DB_NAME} created.")
    else:
        print(f"Database {DB_NAME} already exists.")

    # Bağlantıyı kapat
    cur.close()
    conn.close()
'''

def createDB():
    app = createApp()
    with app.app_context():
        #check_and_create_database()
        db.create_all()
