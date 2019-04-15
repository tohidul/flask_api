from shared.models import db, ma

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = user_email = db.Column(db.String(80), unique=True, nullable=False)
    user_email = db.Column(db.String(80), unique=True, nullable=False)
    user_password = db.Column(db.String(200), nullable=False)
    role_id = db.Column(db.Integer, nullable=False)

    def __init__(self, user_name, user_email, user_password, role_id):
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password
        self.role_id = role_id

    def __repr__(self):
        return '<User %r>' %self.user_name


class UserSchema(ma.Schema):
	class Meta:
		fields = ('id', 'user_name', 'user_email', 'user_password', 'role_id')

