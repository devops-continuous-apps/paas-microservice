from flask import Blueprint, request, jsonify
from ..commands.add_to_blacklist_command import AddToBlacklistCommand
from ..commands.check_blacklist_command import CheckBlacklistCommand
from ..errors.errors import InvalidParams


blacklist_blueprint = Blueprint('blacklist', __name__)


@blacklist_blueprint.route('/blacklists', methods=['POST'])
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
def check_blacklist(email):
    check_blacklist_command = CheckBlacklistCommand(email)
    is_blocked, blocked_reason = check_blacklist_command.execute()

    return jsonify({
        'email': email,
        'blocked': is_blocked,
        'blocked_reason': blocked_reason
    }), 200
