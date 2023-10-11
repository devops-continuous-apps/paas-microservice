from ..commands.add_to_blacklist_command import AddToBlacklistCommand
from ..commands.check_blacklist_command import CheckBlacklistCommand
from ..errors.errors import InvalidParams, InvalidToken
from flask import Blueprint, request, jsonify
from functools import wraps

auth_token = "1234567890"
blacklist_blueprint = Blueprint('blacklist', __name__)


def require_token(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token == f'Bearer {auth_token}':
            return func(*args, **kwargs)
        else:
            raise InvalidToken()
    return decorated_function


@blacklist_blueprint.route('/blacklists', methods=['POST'])
@require_token
def add_to_blacklist():
    data = request.json
    email = data.get('email')
    app_uuid = data.get('app_uuid')
    blocked_reason = data.get('blocked_reason')

    if not email or not app_uuid:
        raise InvalidParams()

    add_to_blacklist_command = AddToBlacklistCommand(
        email,
        app_uuid,
        blocked_reason,
    )
    result = add_to_blacklist_command.execute()
    return jsonify(result), 201


@blacklist_blueprint.route('/blacklists/<string:email>', methods=['GET'])
@require_token
def check_blacklist(email):
    check_blacklist_command = CheckBlacklistCommand(email)
    is_blocked, blocked_reason = check_blacklist_command.execute()

    return jsonify({
        'email': email,
        'blocked': is_blocked,
        'blocked_reason': blocked_reason
    }), 200
