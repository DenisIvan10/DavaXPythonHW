from functools import wraps
from flask import request, jsonify

VALID_TOKENS = {
    "token123": "alice@endava.com",
    "token456": "bob@endava.com",
}

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Missing or invalid Authorization header"}), 401
        
        token = auth_header.replace("Bearer ", "", 1)
        user = VALID_TOKENS.get(token)
        if not user:
            return jsonify({"error": "Invalid token"}), 401
        request.user = user
        return f(*args, **kwargs)
    return decorated

def get_current_user():
    return getattr(request, 'user', None)
