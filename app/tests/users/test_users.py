def test_list_users_unauthorized(api_client):
    response = api_client.get("/api/v1/users/")
    assert response.status_code == 401
