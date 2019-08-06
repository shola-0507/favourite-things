from flask import (Blueprint, request, g)
from flaskr import db
from flaskr.models import Item, items_schema, item_schema, Category, AuditLog
from flaskr.logic import auditTypes, userLogic
from flaskr.system import Utilities
from flaskr.system import HttpResponse

bp = Blueprint('item', __name__, url_prefix='/item')


@bp.route('/create', methods=["POST"])
def create():
    required = {"title": {'type': 'string', 'required': True},
                "description": {'type': 'string', 'required': False},
                "category_id": {'type': 'integer', 'required': True},
                "meta": {'required': False}}

    validate = Utilities.validate(required, request.json)
    if validate is not None:
        return HttpResponse.error_response(validate)

    title = request.json['title']
    category_id = int(request.json['category_id'])
    description = None
    encrypted_user_id = None
    meta = None

    if "meta" in request.json:
        metadata = request.json["meta"]
        allowed_types = ["string", "integer", "date", "enum"]

        meta = Utilities.validate_meta(metadata, allowed_types)
        if "error" in meta:
            return HttpResponse.error_response(meta)

    if "description" in request.json:
        description = str(request.json["description"])

    category = Category.query.filter_by(id=category_id).first()
    if not category:
        return HttpResponse.error_response({"error": "category doesn't exist"})

    if g.user_id is not None:
        user_id = g.user_id
    else:
        user = userLogic.set_userId()
        user_id = user["user_id"]
        encrypted_user_id = user["encrypted_user_id"]

    rank = Item.query.filter_by(user_id=user_id, category_id=category_id).count() + 1
    new_item = Item(user_id, title, description, rank, category_id, meta)
    log_data = AuditLog(user_id, auditTypes.ITEM_CREATED)

    db.session.add(new_item)
    db.session.add(log_data)
    db.session.commit()
    response = item_schema.jsonify(new_item)

    if encrypted_user_id:
        response.set_cookie("user_id", encrypted_user_id)
    return HttpResponse.success_response(response)


@bp.route('/<id>/all', methods=["GET"])
def get_items(id):
    if not g.user_id:
        return HttpResponse.error_response({"error": "You haven't created any items in this category."})

    user_id = g.user_id

    items = Item.query.filter_by(user_id=user_id, category_id=id).order_by(Item.rank).all()
    if not items:
        return HttpResponse.error_response({"error": "You haven't created any items in this category."})

    result = items_schema.dump(items)
    data = result.data

    return HttpResponse.success_response(data)


@bp.route('/<id>/get', methods=["GET"])
def get_item(id):
    if not g.user_id:
        return HttpResponse.error_response({"error": "No matching product found."})

    user_id = g.user_id
    item = Item.query.filter_by(id=id, user_id=user_id).first()

    if not item:
        return HttpResponse.error_response({"error": "No matching Item found"})

    return item_schema.jsonify(item)


@bp.route('/<id>/rank', methods=["PUT"])
def update_ranking(id):
    if not g.user_id:
        return HttpResponse.error_response({"error": "Please create items to be ranked"})

    user_id = g.user_id

    required = {"items": {"required": True}}

    validate = Utilities.validate(required, request.json)
    if validate is not None:
        return HttpResponse.error_response(validate)

    items = request.json["items"]
    rank = 0

    for item_id in items:
        try:
            int(item_id)
        except:
            return HttpResponse.error_response({"error": "Please send the ids of the items as integers"})

        item = Item.query.filter_by(id=item_id, user_id=user_id, category_id=id).first()
        if item:
            rank = rank + 1
            item.rank = rank
            db.session.commit()

    log_data = AuditLog(user_id, auditTypes.RANKING_UPDATED)
    db.session.add(log_data)
    db.session.commit()

    items = Item.query.filter_by(user_id=user_id, category_id=id).order_by(Item.rank).all()
    result = items_schema.dump(items)
    return HttpResponse.success_response(result.data)


@bp.route('/<id>/update', methods=["PUT"])
def update_item(id):

    if not g.user_id:
        return HttpResponse.error_response({"error": "No matching product found."})

    required = {"title": {"type": "string", "required": False},
                "description": {"type": "string", "required": False},
                "category_id": {"type": "integer", "required": False}}

    validate = Utilities.validate(required, request.json)
    if validate is not None:
        return HttpResponse.error_response(validate)

    user_id = g.user_id
    item = Item.query.filter_by(id=id, user_id=user_id).first()

    if not item:
        return HttpResponse.error_response({"error": "No matching item found"})

    title = item.title
    description = item.description
    category_id = item.category_id
    rank = None

    if "title" in request.json:
        title = request.json["title"]

    if "description" in request.json:
        description = request.json["description"]

    if "category_id" in request.json and request.json["category_id"] != category_id:
        category = Category.query.filter_by(id=request.json["category_id"]).first()
        if not category:
            return HttpResponse.error_response({"error": "category doesn't exist"})

        category_id = request.json["category_id"]
        rank = Item.query.filter_by(user_id=user_id, category_id=category_id).count() + 1

    item.title = title
    item.description = description
    item.category_id = category_id

    if rank is not None:
        item.rank = rank

    log_data = AuditLog(user_id, auditTypes.ITEM_UPDATED)
    db.session.add(log_data)
    db.session.commit()
    response = item_schema.jsonify(item)

    return HttpResponse.success_response(response)


@bp.route('/<id>/delete', methods=["DELETE"])
def delete(id):
    if not g.user_id:
        HttpResponse.success_response({"error": "Please create the item first"})

    user_id = g.user_id

    item = Item.query.filter_by(id=id, user_id=user_id).first()

    if not item:
        return HttpResponse.error_response({"error": "No item found"})

    db.session.delete(item)

    log_data = AuditLog(user_id, auditTypes.ITEM_DELETED)
    db.session.add(log_data)
    db.session.commit()

    data = item_schema.jsonify(item)
    return HttpResponse.success_response(data)


@bp.before_request
def get_user():
    if "user_id" in request.cookies:
        id = request.cookies.get('user_id')
        user = userLogic.get_userId(id)

        if user is not None:
            g.user_id = user.id
        else:
            g.user_id = None
    else:
        g.user_id = None
