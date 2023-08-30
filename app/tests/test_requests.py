def test_request(client):
    response = client.get('/get-mean')
    assert b'The mean of the concentration' in response.data

def test_request(client):
    response = client.get('/get-std-deviation')
    assert b'The standard deviation of the concentration' in response.data

def test_request(client):
    response = client.get('/get-sum')
    assert b'The total sum of the concentration' in response.data