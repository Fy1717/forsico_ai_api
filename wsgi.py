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


if __name__ == '__main__':
    HOST = os.getenv('FLASK_HOST', '127.0.0.1')  # Default to localhost
    DEBUG_MODE = os.getenv('FLASK_DEBUG', 'False') == 'True'
    app.run(debug=DEBUG_MODE, host=HOST, port=5001)
