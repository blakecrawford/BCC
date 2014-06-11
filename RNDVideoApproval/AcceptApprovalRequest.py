import viaRabbitDev
import ast
import json
from flask import Flask
from flask import jsonify
from flask import request
from flask import abort
from flask import make_response

app = Flask(__name__)

@app.route('/')
def index():
    return "Research & Development Mobile Video Approval Request Service"

@app.route('/rest/approval/request', methods=['POST'])
def enqueue_request():
    if not request.json:
        abort(make_response("The entire body of the request is malformed.\n", 400))
    if not request.json.get('videoURL') or type(request.json['videoURL']) is not unicode:
        abort(make_response("The videoURL is missing or malformed.\n", 400))
    if not request.json.get('dueDate') or type(request.json['dueDate']) is not unicode:
        abort(make_response("The dueDate is missing or malformed.\n", 400))
    if not request.json.get('requestor') or type(request.json['requestor']) is not unicode:
        abort(make_response("The requestor is missing or malformed.\n", 400))
    channel = viaRabbitDev.get_dev_channel('/mqPlaypen')
    channel.basic_publish(exchange='videoApproval', routing_key='video.approval', body=json.dumps(request.json))
    channel.close()
    return jsonify({'status': 'OK'})

if __name__ == '__main__':
    app.run(debug=True)




