from shared.models import db,ma
from models.role_model import Role, RoleSchema
from flask import jsonify
role_schema = RoleSchema(strict=True)
roles_schema = RoleSchema(many=True, strict=True)

def add_role(role_name):
    new_role = Role(role_name)
    
    check_role = Role.query.filter_by(role_name=role_name).first()

    if check_role is None:
        db.session.add(new_role)
        db.session.commit()

        response = {
            "success": True
        }
    else:
        response = {
            "success": False
        }
    return response

def get_all_roles():
    Roles = Role.query.all()
    result = roles_schema.dump(Roles)

    if(result):
        return result.data
    else:
        return {
            "message": "no data fetched"
        }


def get_role_by_role_id(role_id):
    role = Role.query.filter_by(id=role_id).first()
    if role is None:
        return jsonify(role)
    else:
        return role_schema.jsonify(role)
        
def update_role_by_id(role_id, new_role_name):

    role_to_update = Role.query.filter_by(id=role_id).first()
    if role_to_update:
        role_to_update.role_name=new_role_name
        db.session.commit()
        return {'success':True}
        
    else:
        return {'success':False}

def delete_role_by_id(role_id):
    if(Role.query.filter_by(id=role_id).delete()):
        db.session.commit()
        return {'success':True}
    else:
        return {'success':False}