import time

from flask import Blueprint, jsonify

blueprint = Blueprint('hello', __name__)

@blueprint.route('/api/hello', methods=('GET', ))
def get_hello():
    query = request.args

    sleep_time = int(query.get('sleep_time', '0'))
    if sleep_time > 0:
        time.sleep(sleep_time)

    res = {
        'value': 'Hello World',
        'sleep_time': sleep_time,
    }
    return jsonify(res)
