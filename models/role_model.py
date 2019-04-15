from shared.models import db, ma
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, role_name):
        self.role_name = role_name

    def __repr__(self):
        return '<Role %r>' %self.role_name


class RoleSchema(ma.Schema):
	class Meta:
		fields = ('id', 'role_name')

