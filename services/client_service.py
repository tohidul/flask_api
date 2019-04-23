from shared.models import db,ma
from models.client_model import Client, ClientSchema
from flask import jsonify
client_schema = ClientSchema(strict=True)
clients_schema = ClientSchema(many=True, strict=True)

def construct_new_client(cid,client_name,client_description):
    new_client = Client(cid, client_name, client_description)
    return new_client


def add_client(cid,client_name,client_description):
    new_client = construct_new_client(cid, client_name, client_description)
    
    check_client = Client.query.filter_by(cid=cid).first()

    if check_client is None:
        db.session.add(new_client)
        db.session.commit()

        response = {
            "success": True
        }
    else:
        response = {
            "success": False
        }
    return response

def get_all_clients():
    clients = Client.query.all()
    result = clients_schema.dump(clients)
    

    if(clients):
        return result.data
    else:
        return {
            "message": "no data fetched"
        }


def get_client_by_cid(cid):
    client = Client.query.filter_by(cid=cid).first()
    if client is None:
        return jsonify(client)
    else:
        return client_schema.jsonify(client)
        
def update_client_by_id(id, new_cid, new_client_name, new_client_description):

    client_to_update = Client.query.filter_by(id=id).first()
    if client_to_update:
        client_to_update.cid=new_cid
        client_to_update.client_description = new_client_description
        client_to_update.client_name=new_client_name
        #print('------------2222-------------')
        db.session.commit()
        return {'success':True}
        
    else:
        return {'success':False}

def delete_client_by_id(id):

    if(Client.query.filter_by(id=id).delete()):
        db.session.commit()
        return {'success':True}
    else:
        return {'success':False}