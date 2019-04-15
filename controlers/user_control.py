from models.user_model import User
from flask import Blueprint


account_api2 = Blueprint('account_api',__name__)

# user_schema = UserSchema(strict = True)
# users_schema = UserSchema(many = True, strict = True)

# @user_api.route('/api/user',methods=['POST'])
# def add_user():
#     user_name = request.json['user_name']
#     user_email = request.json['user_email']
#     user_password = request.json['user_password']
#     role_id = request.json['role_id']

#     new_user = User(user_name,user_email,user_password,role_id)
#     db.session.add(new_user)
#     db.session.commit()

    # return user_schema.jsonify(new_user)

@account_api2.route('/api/user', methods=['GET'])
def get_all_user_():
    return "Hello"
    # all_user = User.query.all()
    # result = users_schema.dump(all_user)
    # return jsonify(result.data)


# @user_api.route('/api/user/<id>', methods=['GET'])
# def get_user_by_id(id):
#     user = User.query.get(id)
#     return user_schema.jsonify(user)

# @user_api.route('/api/user/<id>', methods=['DELETE'])
# def delete_user(id):
#     user = User.query.get(id)
#     db.session.delete(user)
#     db.session.commit()

#     return user_schema.jsonify(user)