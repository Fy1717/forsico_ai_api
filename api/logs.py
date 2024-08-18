
# from app.auth import token_required
from app.models import read_logs, update_log, delete_log
from flask import Blueprint, request, jsonify

api_logs = Blueprint('logs', __name__, url_prefix="/api/logs")


@api_logs.route('/all', methods=['GET'])
# @token_required
def read_all_logs():
    log_list = read_logs()
    if log_list:
        return jsonify({"data": [log.to_dict() for log in log_list]})
    return jsonify(error="Logs not found"), 404


'''

@api_logs.route('/<int:log_id>', methods=['GET'])
@token_required
def read_log_endpoint(log_id): #current_user,
    log = read_log(log_id)
    if log:
        return jsonify(log_id=log.id, task_id=log.task_id, response_text=log.response_text)
    return jsonify(error="Log not found"), 404
'''


@api_logs.route('/<int:log_id>', methods=['PUT'])
# @token_required
def update_log_endpoint(current_user, log_id):
    new_response_text = request.json.get('response_text')
    log = update_log(log_id, new_response_text)
    if log:
        return jsonify(log_id=log.id, task_id=log.task_id, 
                       response_text=log.response_text)
    return jsonify(error="Failed to update log"), 500


@api_logs.route('/<int:log_id>', methods=['DELETE'])
# @token_required
def delete_log_endpoint(log_id):  
    if delete_log(log_id):
        return jsonify(success=True), 200
    return jsonify(error="Failed to delete log"), 500
