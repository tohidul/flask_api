from models.client_model import Client, ClientSchema
from flask import Blueprint
from services import client_service
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 

client_api = Blueprint('client_api',__name__)

client_schema = ClientSchema(strict = True)
clients_schema = ClientSchema(many = True, strict = True)

@client_api.route('/api/clients', methods=['POST'])
def add_client():
    cid = request.json['cid']
    client_name = request.json['client_name']
    client_description = request.json['client_description']

    response = client_service.add_client(cid,client_name,client_description)

    # new_user = User(user_name,user_email,user_password,role_id)
    # db.session.add(new_user)
    # db.session.commit()

    return jsonify(response)


@client_api.route('/api/clients', methods=['GET'])
def get_all_clients():

    response = client_service.get_all_clients()

    # new_user = User(user_name,user_email,user_password,role_id)
    # db.session.add(new_user)
    # db.session.commit()

    return jsonify(response)

@client_api.route('/api/clients/<cid>', methods=['GET'])
def get_client_by_cid(cid):

    response = client_service.get_client_by_cid(cid)

    # new_user = User(user_name,user_email,user_password,role_id)
    # db.session.add(new_user)
    # db.session.commit()

    return response

@client_api.route('/api/clients/<id>', methods=['PUT'])
def update_client_by_id(id):

    new_cid = request.json['cid']
    new_client_name = request.json['client_name']
    new_client_description = request.json['client_description']
    #print(cid+'222222222')
    response = client_service.update_client_by_id(id, new_cid, new_client_name, new_client_description)

    # new_user = User(user_name,user_email,user_passwordole_id)
    # db.session.add(new_user)
    # db.session.commit()

    return jsonify(response)

@client_api.route('/api/clients/<id>', methods=['DELETE'])
def delete_client_by_cid(id):

    #print(cid+'222222222')
    response = client_service.delete_client_by_id(id)

    # new_user = User(user_name,user_email,user_passwordole_id)
    # db.session.add(new_user)
    # db.session.commit()

    return jsonify(response)
