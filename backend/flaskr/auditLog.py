from flask import (Blueprint, request, g)
from flaskr.models import  AuditLog, audit_logs_schema
from flaskr.system import HttpResponse, Utilities
from flaskr.logic import auditTypes, userLogic


bp = Blueprint('auditLog', __name__, url_prefix='/logs')


@bp.route('/get', methods=["get"])
def get_logs():
    if not g.user_id:
        return HttpResponse.error_response({"error": "You haven't performed any actions yet."}, 404)

    user_id = g.user_id
    logs = AuditLog.query.filter_by(user_id=user_id).all()
    if not logs:
        return HttpResponse.error_response({"error": "You haven't performed any actions yet."}, 404)

    result = audit_logs_schema.dump(logs)
    data = result.data

    return HttpResponse.success_response(data)


@bp.before_request
def get_user():
    if "user_id" in request.cookies:
        id = request.cookies.get('user_id')
        user = userLogic.get_userId(id)
        if user:
            g.user_id = user.id
        else:
            g.user_id = None
    else:
        g.user_id = None
