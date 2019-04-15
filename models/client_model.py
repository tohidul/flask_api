from shared.models import db, ma
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cid = db.Column(db.String(80), unique=True, nullable=False)
    client_name = db.Column(db.String(80), nullable=False)
    client_description = db.Column(db.String(600), nullable=True)

    def __init__(self, cid, client_name, client_description):
        self.cid = cid
        self.client_name = client_name
        self.client_description = client_description

    def __repr__(self):
        return '<Client %r>' %self.client_name


class ClientSchema(ma.Schema):
	class Meta:
		fields = ('id', 'cid', 'client_name', 'client_description')

