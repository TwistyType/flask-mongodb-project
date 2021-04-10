from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash


class Template(db.Document):
    template_name = db.StringField(required=True)
    subject = db.StringField(required=True)
    body = db.StringField(required=True)
    added_by = db.ReferenceField('User')


class User(db.Document):
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)
    templates = db.ListField(db.ReferenceField(
        'Template', reverse_delete_rule=db.PULL))

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf-8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


# another delete rule which ensures that if a user is deleted,
# then the owned templates are also deleted
User.register_delete_rule(Template, 'added_by', db.CASCADE)
