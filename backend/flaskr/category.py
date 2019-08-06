from flask import (Blueprint, request, g)
from flaskr.models import Category, categories_schema, category_schema, AuditLog
from flaskr import db
from flaskr.system import HttpResponse, Utilities
from flaskr.logic import auditTypes, userLogic


bp = Blueprint('category', __name__, url_prefix='/category')


@bp.route('/create', methods=["POST"])
def create():
    encrypted_user_id = None

    required = {"name": {'type': 'string', 'required': True}}

    validate = Utilities.validate(required, request.json)
    if validate is not None:
        return HttpResponse.error_response(validate)

    if g.user_id is not None:
        user_id = g.user_id
    else:
        user = userLogic.set_userId()
        user_id = user["user_id"]
        encrypted_user_id = user["encrypted_user_id"]

    name = str(request.json['name']).lower()

    new_category = Category(name, user_id)
    log_data = AuditLog(user_id, auditTypes.CATEGORY_CREATED)
    db.session.add(new_category)
    db.session.add(log_data)
    db.session.commit()

    response = category_schema.jsonify(new_category)
    if encrypted_user_id is not None:
        response.set_cookie("user_id", encrypted_user_id)
    return HttpResponse.success_response(response)


@bp.route('/all', methods=["GET"])
def read_all():
    categories = Category.query.all()

    if not categories:
        return HttpResponse.error_response({"error": "No category found"})

    result = categories_schema.dump(categories)
    response = result.data
    return HttpResponse.success_response(response)


@bp.route('/<id>/get', methods=["GET"])
def read(id):
    category = Category.query.get(id)

    if not category:
        return HttpResponse.error_response({"error": "Category not found"})

    response = category_schema.jsonify(category)
    return HttpResponse.success_response(response)


@bp.route('/<id>/update', methods=["PUT"])
def update(id):
    category = Category.query.get(id)

    if not category:
        return HttpResponse.error_response({"error": "Category not found"})

    name = request.json['name']
    category.name = name if name else category.name
    db.session.commit()

    response = category_schema.jsonify(category)
    return HttpResponse.success_response(response)


@bp.route('/<id>/delete', methods=["DELETE"])
def delete(id):
    category = Category.query.get(id)

    if not category:
        return HttpResponse.error_response({"error": "Category not found"})

    db.session.delete(category)
    db.session.commit()
    response = category_schema.jsonify(category)
    return HttpResponse.success_response(response)


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
