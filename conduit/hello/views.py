from flask import Blueprint, jsonify

blueprint = Blueprint('hello', __name__)

@blueprint.route('/api/hello', methods=('GET', ))
def get_hello():
    return jsonify({'value': 'Hello World'})
