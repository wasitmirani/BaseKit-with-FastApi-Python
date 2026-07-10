def test_register_validation(api_client):
    response = api_client.post(
        "/api/v1/auth/register",
        json={"email": "invalid-email", "password": "short"},
    )
    assert response.status_code == 422
