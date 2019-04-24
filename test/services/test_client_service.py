from shared.models import db,ma
from models.client_model import Client
from services import client_service
from sqlalchemy import create_engine
import pytest
from unittest import mock
from mock import patch

def test_construct_new_client():
    new_client = client_service.construct_new_client('comm', 'community', 'credit union')

    assert new_client.cid == 'comm'
    assert new_client.client_name == 'community'
    assert new_client.client_description == 'credit union'



# def test_func1():
#     ret = func1()
#     assert ret == 3

mocked_data_all_clients = [
    {
        "cid": "test use1r",
        "client_description": "123",
        "client_name": "rre@s1d.com",
        "id": 1
    },
    {
        "cid": "e1r",
        "client_description": "123",
        "client_name": "rre@s1d.com",
        "id": 2
    },
    {
        "cid": "e11212r",
        "client_description": "123",
        "client_name": "rre@s1d.com",
        "id": 3
    },
    {
        "cid": "amac",
        "client_description": "a credit union",
        "client_name": "asdfqwer",
        "id": 4
    }
]

#@pytest.mark.parametrize('data', [mocked_data_all_clients, {}])
@patch('Client.query.all')
def test_get_all_clients(mock_all):
    mock_all.return_value = mocked_data_all_clients
    a = client_service.get_all_clients()
    if a:
        assert a == mocked_data_all_clients
    else:
        assert a == {
            "message": "no data fetched"
        }
