from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from shared.models import db,ma
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
CORS(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# ma = Marshmallow(app)

#from routes.user_route import account_api2
from controlers.client_control import client_api
from controlers.role_control import role_api





if __name__ == "__main__":
    
#app.register_blueprint(account_api2)
    db.app=app
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # db.init_app(app)
    app.register_blueprint(client_api)
    app.register_blueprint(role_api)
    
    app.run(host="0.0.0.0", debug=True)
