from flaskr import db, ma
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(80), nullable=False)
    items = db.relationship('Item', backref=db.backref('user', lazy=True))
    categories = db.relationship('Category', backref=db.backref('user', lazy=True))
    auditLogs = db.relationship('AuditLog', backref=db.backref('user', lazy=True))
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, user_id):
        self.user_id = user_id


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'created_date')


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    items = db.relationship('Item', backref=db.backref('category', lazy=True))
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id


class CategorySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'created_date')


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    rank = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    meta = db.Column(db.JSON, nullable=True)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    modified_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, user_id, title, description, rank, category_id, meta=None):
        self.user_id = user_id
        self.title = title
        self.description = description
        self.rank = rank
        self.category_id = category_id
        self.meta = meta


class ItemSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'rank', 'category_id',
                  'created_date', 'modified_date', 'meta')


class AuditLog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    action = db.Column(db.String(80), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, user_id, action):
        self.user_id = user_id
        self.action = action


class AuditLogSchema(ma.Schema):
    class Meta:
        fields = ('id', 'action', 'date')


user_schema = UserSchema(strict=True)

category_schema = CategorySchema(strict=True)
categories_schema = CategorySchema(many=True, strict=True)

item_schema = ItemSchema(strict=True)
items_schema = ItemSchema(many=True, strict=True)

audit_log_schema = AuditLogSchema(strict=True)
audit_logs_schema = AuditLogSchema(many=True, strict=True)
