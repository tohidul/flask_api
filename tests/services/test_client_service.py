from unittest.mock import MagicMock
from models.client_model import Client
from services.client_service import get_all_clients
import pytest

@mock.path("Client")
def test_client(self, mock_client):

    test_client = Client()
    test_client.cid = 'test_cid'
    test_client.client_description = 'aa qq ee'
    test_client.client_name = 'test name'
    test_client.id = 1

    mock_client.query.all.return_value = [test_client]

    a = get_all_clients()
    assert(a)
