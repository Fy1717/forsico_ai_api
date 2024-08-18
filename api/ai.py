# import transformers
# from app.auth import token_required
from flask import Blueprint, request, jsonify
from app.models import create_log
api_ai = Blueprint('ai', __name__, url_prefix="/api/ai")

# Modeli yükle
'''
model_id_en = "gpt2"  
# Örnek olarak GPT-2 İngilizce modeli
model_id_tr = "dbmdz/bert-base-turkish-cased"  
# Örnek olarak BERT Türkçe modeli

model_en = transformers.pipeline("text-generation", model=model_id_en, device=0)
model_tr = transformers.pipeline("text-generation", model=model_id_tr, device=0)
'''


@api_ai.route('/generate', methods=['POST'])
# @token_required
def generate_text():
    default_result_object = {
        "tasks": [
            {
                "id": 201,
                "key": "API Development",
                "description": "Build RESTful APIs for user handling.",
                "title": "Backend Development"
            },
            {
                "id": 202,
                "key": "Database Optimization",
                "description": "Optimize database queries and indices for performance.",
                "title": "Backend Development"
            },
            {
                "id": 203,
                "key": "Security Enhancements",
                "description": "Implement API security measures, including rate limiting and logging.",
                "title": "Backend Development"
            },
            {
                "id": 204,
                "key": "Session Management",
                "description": "Develop secure session management for user authentication.",
                "title": "Backend Development"
            },
            {
                "id": 205,
                "key": "Cloud Integration",
                "description": "Setup cloud storage solutions for scalable data handling.",
                "title": "Backend Development"
            },
            {
                "id": 101,
                "key": "Navbar Design",
                "description": "Design a responsive navigation bar.",
                "title": "Frontend Development"
            },
            {
                "id": 102,
                "key": "Footer Component",
                "description": "Develop a footer component with links and contact info.",
                "title": "Frontend Development"
            },
            {
                "id": 103,
                "key": "Form Validation",
                "description": "Implement client-side form validation.",
                "title": "Frontend Development"
            },
            {
                "id": 104,
                "key": "Accessibility Features",
                "description": "Ensure all frontend components meet accessibility standards.",
                "title": "Frontend Development"
            },
            {
                "id": 105,
                "key": "Theme Integration",
                "description": "Create a light and dark mode toggle.",
                "title": "Frontend Development"
            }
        ]
    }
    
    input_text = request.json.get('text', '')
    # language = request.json.get('lang', 'en')  
    # # Varsayılan dil İngilizce olarak ayarlanmıştır.

    if not input_text:
        return jsonify({'error': 'No text provided'}), 400

    create_log(0, str(default_result_object))
    
    return jsonify({'data': default_result_object})