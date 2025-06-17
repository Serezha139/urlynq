from flask import Blueprint, request, abort

main = Blueprint('main', __name__)

USERNAME = 'admin'
PASSWORD = 'secret'


@main.route('/', methods=['GET'])
def index():
    return "<h1>Hello, Flask!</h1>"


@main.route('/process', methods=['POST'])
def process_string():
    # Basic Auth
    auth = request.authorization
    if not auth or auth.username != USERNAME or auth.password != PASSWORD:
        return ('Unauthorized', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

    # Handle JSON
    data = request.get_json()
    if not data or 'text' not in data:
        abort(400, description="Missing 'text' in request JSON")

    text = data['text']
    print(f"Received text: {text}")

    return '', 204
