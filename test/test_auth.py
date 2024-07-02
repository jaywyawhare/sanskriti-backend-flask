import pytest

@pytest.mark.run(order=1)
def test_register(client, db_session):
    response = client.post('/auth/register', json={
        'email': 'testuser@example.com',
        'password': 'password'
    })
    assert response.status_code == 201
    assert 'access_token' in response.get_json()

@pytest.mark.run(order=2)
def test_login(client, init_db):
    response = client.post('/auth/login', json={
        'email': 'admin@example.com',
        'password': 'admin'
    })
    assert response.status_code == 200
    assert 'access_token' in response.get_json()

@pytest.mark.run(order=3)
def test_logout(client, init_db):
    login_response = client.post('/auth/login', json={
        'email': 'admin@example.com',
        'password': 'admin'
    })
    access_token = login_response.get_json()['access_token']
    
    response = client.get('/auth/logout', headers={'Authorization': f'Bearer {access_token}'})
    assert response.status_code == 200
    assert response.get_json()['message'] == 'Successfully logged out'

@pytest.mark.run(order=4)
def test_get_me(client, init_db):
    login_response = client.post('/auth/login', json={
        'email': 'admin@example.com',
        'password': 'admin'
    })
    access_token = login_response.get_json()['access_token']

    response = client.get('/auth/me', headers={'Authorization': f'Bearer {access_token}'})
    assert response.status_code == 200
    assert response.get_json()['email'] == 'admin@example.com'
