import os
from flask_cors import CORS
from app import createApp
from api.ai import api_ai
from api.logs import api_logs
from app.initialize_db import createDB

app = createApp()
CORS(app)
createDB()

app.register_blueprint(api_ai)
app.register_blueprint(api_logs)


@app.route('/')
def hello_geek():
    return '<h1>Hello FORSICO</h2>'


if os.getenv('FLASK_ENV') == 'development':
    host = "0.0.0.0"
else:
    host = "127.0.0.1"

if __name__ == '__main__':
    FLASK_ENV = os.getenv('FLASK_ENV', 'production')  # Default to production for safety
    host = "0.0.0.0" if FLASK_ENV == 'development' else "127.0.0.1"
    DEBUG_MODE = os.getenv('FLASK_DEBUG', 'False') == 'True'
    app.run(debug=DEBUG_MODE, host=host, port=5001)
