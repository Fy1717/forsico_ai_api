import logging
from logging.handlers import RotatingFileHandler
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Logger'ı yapılandır
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=5)
formatter = logging.Formatter('%(asctime)s - %(name)s - ' 
                              + '%(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

db = SQLAlchemy()


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    response_text = db.Column(db.Text, nullable=False)
    
    def to_dict(self):
        return {
            "id": self.id,
            "task_id": self.task_id,
            "created_at": self.created_at,
            "response_text": self.response_text,
        }

# CRUD işlemleri ve diğer fonksiyonlar buraya eklenebilir


# Log CRUD
def create_log(task_id, response_text):
    try:
        log = Log(task_id=task_id, response_text=response_text)
        db.session.add(log)
        db.session.commit()
        
        # print("log created : " + response_text)
        
        return log
    except Exception as e:
        # print("error : " + str(e))
        db.session.rollback()
        
        log_error(f"Error creating log: {e}")
        return None
        
        
def read_logs():
    try:
        logs = Log.query.all()
        
        return logs
    except Exception as e:
        log_error(f"Error reading log: {e}")
        return None
    

def read_log(log_id):
    try:
        log = Log.query.get(log_id)
        return log
    except Exception as e:
        log_error(f"Error reading log: {e}")
        return None


def update_log(log_id, new_response_text):
    try:
        log = Log.query.get(log_id)
        if log:
            log.response_text = new_response_text
            db.session.commit()
            return log
        return None
    except Exception as e:
        db.session.rollback()
        log_error(f"Error updating log: {e}")
        return None


def delete_log(log_id):
    try:
        log = Log.query.get(log_id)
        if log:
            db.session.delete(log)
            db.session.commit()
            return True
        return False
    except Exception as e:
        db.session.rollback()
        log_error(f"Error deleting log: {e}")
        return False


def log_error(message):
    """Log hata mesajlarını dosyaya ve konsola yazdır."""
    logger.error(message)