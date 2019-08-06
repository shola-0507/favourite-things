from flaskr.models import User
from flaskr import db
from cryptography.fernet import Fernet
from flaskr.system import config
from flaskr.system import Utilities


f = Fernet(config["key"])


class userLogic:
    @staticmethod
    def get_userId(id):
        bytes_id = bytes(id, encoding='utf8')
        user_id = f.decrypt(bytes_id)
        user = User.query.filter_by(user_id=user_id).first()
        if user:
            return user
        else:
            return None

    @staticmethod
    def set_userId():
        response = {"user_id": None, "encrypted_user_id": None}
        _id = Utilities.rand_string(10)
        encrypted_user_id = f.encrypt(_id.encode('utf-8'))
        user = userLogic.register_user(_id)

        response["user_id"] = user.id
        response["encrypted_user_id"] = encrypted_user_id
        return response

    @staticmethod
    def register_user(id):
        new_user = User(user_id=id)
        db.session.add(new_user)
        db.session.commit()

        user = User.query.filter_by(user_id=id).first()
        return user
