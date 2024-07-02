def test_get_users(client, init_db):
    login_response = client.post('/auth/login', json={
        'email': 'admin@example.com',
        'password': 'admin'
    })
    access_token = login_response.get_json()['access_token']

    response = client.get('/users/', headers={'Authorization': f'Bearer {access_token}'})
    assert response.status_code == 200
    assert len(response.get_json()) > 0

def test_get_user(client, init_db):
    login_response = client.post('/auth/login', json={
        'email': 'admin@example.com',
        'password': 'admin'
    })
    access_token = login_response.get_json()['access_token']

    response = client.get('/users/1', headers={'Authorization': f'Bearer {access_token}'})
    assert response.status_code == 200
    assert response.get_json()['email'] == 'admin@example.com'

def test_create_user(client, init_db):
    login_response = client.post('/auth/login', json={
        'email': 'admin@example.com',
        'password': 'admin'
    })
    access_token = login_response.get_json()['access_token']

    response = client.post('/users/', headers={'Authorization': f'Bearer {access_token}'}, json={
        'email': 'newuser@example.com',
        'password': 'newpassword',
        'role': 'contributor'
    })
    assert response.status_code == 201
    assert response.get_json()['email'] == 'newuser@example.com'

def test_update_user(client, init_db):
    login_response = client.post('/auth/login', json={
        'email': 'admin@example.com',
        'password': 'admin'
    })
    access_token = login_response.get_json()['access_token']

    response = client.put('/users/1', headers={'Authorization': f'Bearer {access_token}'}, json={
        'email': 'updatedadmin@example.com',
        'password': 'updatedpassword',
        'role': 'admin'
    })
    assert response.status_code == 200
    assert response.get_json()['email'] == 'updatedadmin@example.com'

def test_delete_user(client, init_db):
    login_response = client.post('/auth/login', json={
        'email': 'admin@example.com',
        'password': 'admin'
    })
    access_token = login_response.get_json()['access_token']

    response = client.delete('/users/1', headers={'Authorization': f'Bearer {access_token}'})
    assert response.status_code == 200
    assert response.get_json()['message'] == 'User deleted'
