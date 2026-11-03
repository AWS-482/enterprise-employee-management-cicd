from app import create_app


def test_employees():
    app = create_app()
    client = app.test_client()

    response = client.get("/employees")

    assert response.status_code == 200
    assert response.json["total"] == 3


def test_employee_names():
    app = create_app()
    client = app.test_client()

    response = client.get("/employees")

    assert response.json["employees"][0]["name"] == "John"
