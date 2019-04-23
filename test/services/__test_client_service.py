import os
import tempfile

import pytest
import mock
import main
from shared.models import db

@pytest.fixture
def client():
    db_fd, main.app.config['DATABASE'] = tempfile.mkstemp()
    main.app.config['TESTING'] = True
    client = main.app.test_client()


    db.app=main.app
    db.init_app(main.app)

    with main.app.app_context():
        db.create_all()
    yield client

    os.close(db_fd)
    os.unlink(main.app.config['DATABASE'])


def test_client_service(client):
    import services
    from services.client_service import get_all_clients
    services.client_service.Client.query.all = mock.Mock(return_value={})

    print(get_all_clients())