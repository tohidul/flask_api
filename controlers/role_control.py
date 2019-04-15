from models.role_model import Role, RoleSchema
from flask import Blueprint
from services import role_service
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 

role_api = Blueprint('role_api',__name__)

role_schema = RoleSchema(strict = True)
roles_schema = RoleSchema(many = True, strict = True)

@role_api.route('/api/role', methods=['POST'])
def add_role():
    role_name = request.json['role_name']
    
    response = role_service.add_role(role_name)

    return jsonify(response)


@role_api.route('/api/role', methods=['GET'])
def get_all_roles():

    response = role_service.get_all_roles()

    return jsonify(response)

@role_api.route('/api/role/<role_name>', methods=['GET'])
def get_role_by_role_name(role_name):

    response = role_service.get_role_by_role_name(role_name)

    return response

@role_api.route('/api/role/<role_name>', methods=['PUT'])
def update_role_by_name(role_name):

    new_role_name = request.json['role_name']
    response = role_service.update_role_by_name(role_name, new_role_name)

    return jsonify(response)

@role_api.route('/api/role/<role_name>', methods=['DELETE'])
def delete_role_by_name(role_name):

    response = role_service.delete_role_by_name(role_name)

    return jsonify(response)
