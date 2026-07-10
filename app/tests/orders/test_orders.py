def test_list_orders_unauthorized(api_client):
    response = api_client.get("/api/v1/orders/")
    assert response.status_code == 401
