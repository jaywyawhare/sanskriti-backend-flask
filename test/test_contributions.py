def test_get_contributions(client, init_db):
    login_response = client.post('/auth/login', json={
        'email': 'admin@example.com',
        'password': 'admin'
    })
    access_token = login_response.get_json()['access_token']

    response = client.get('/contributions/', headers={'Authorization': f'Bearer {access_token}'})
    assert response.status_code == 200

def test_get_contribution(client, init_db):
    login_response = client.post('/auth/login', json={
        'email': 'admin@example.com',
        'password': 'admin'
    })
    access_token = login_response.get_json()['access_token']

    # Create a contribution first
    client.post('/contributions/', headers={'Authorization': f'Bearer {access_token}'}, json={
        'language': 'Python',
        'question': 'What is FastAPI?',
        'answer': 'FastAPI is a web framework.'
    })

    response = client.get('/contributions/1', headers={'Authorization': f'Bearer {access_token}'})
    assert response.status_code == 200
    assert response.get_json()['question'] == 'What is FastAPI?'

def test_create_contribution(client, init_db):
    login_response = client.post('/auth/login', json={
        'email': 'contributor@example.com',
        'password': 'contributor'
    })
    access_token = login_response.get_json()['access_token']

    response = client.post('/contributions/', headers={'Authorization': f'Bearer {access_token}'}, json={
        'language': 'Python',
        'question': 'What is FastAPI?',
        'answer': 'FastAPI is a web framework.'
    })
    assert response.status_code == 201
    assert response.get_json()['question'] == 'What is FastAPI?'

def test_update_contribution(client, init_db):
    login_response = client.post('/auth/login', json={
        'email': 'contributor@example.com',
        'password': 'contributor'
    })
    access_token = login_response.get_json()['access_token']

    # Create a contribution first
    client.post('/contributions/', headers={'Authorization': f'Bearer {access_token}'}, json={
        'language': 'Python',
        'question': 'What is FastAPI?',
        'answer': 'FastAPI is a web framework.'
    })

    response = client.put('/contributions/1', headers={'Authorization': f'Bearer {access_token}'}, json={
        'language': 'Python',
        'question': 'What is FastAPI?',
        'answer': 'FastAPI is a modern web framework.'
    })
    assert response.status_code == 200
    assert response.get_json()['answer'] == 'FastAPI is a modern web framework.'

def test_delete_contribution(client, init_db):
    login_response = client.post('/auth/login', json={
        'email': 'contributor@example.com',
        'password': 'contributor'
    })
    access_token = login_response.get_json()['access_token']

    # Create a contribution first
    client.post('/contributions/', headers={'Authorization': f'Bearer {access_token}'}, json={
        'language': 'Python',
        'question': 'What is FastAPI?',
        'answer': 'FastAPI is a web framework.'
    })

    response = client.delete('/contributions/1', headers={'Authorization': f'Bearer {access_token}'})
    assert response.status_code == 200
    assert response.get_json()['message'] == 'Contribution deleted'
