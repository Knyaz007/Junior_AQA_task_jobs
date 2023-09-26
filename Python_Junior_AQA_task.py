import requests

def test_get_category_list():
    url = "http://91.210.171.73:8080/api/category/"
    auth = ('admin', 'admin')

    response = requests.get(url, auth=auth)

    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.headers["Content-Type"] == "application/json", "Expected JSON response"

    json_data = response.json()
    assert "count" in json_data
    assert "next" in json_data
    assert "previous" in json_data
    assert "results" in json_data
    assert len(json_data["results"]) > 0, "Expected non-empty list of categories"

def test_create_category():
    url = "http://91.210.171.73:8080/api/category/"
    auth = ('admin', 'admin')

    payload = {
        "id": 1,  # Указываем уникальный ID
        "name": "Test Category"  # Указываем уникальное имя категории
    }

    response = requests.post(url, json=payload, auth=auth)

    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
    assert response.headers["Content-Type"] == "application/json", "Expected JSON response"

    json_data = response.json()
    assert "id" in json_data
    assert "name" in json_data

    # Проверяем, что созданная категория соответствует отправленным данным
    assert json_data["id"] == payload["id"]
    assert json_data["name"] == payload["name"]





def test_get_category_by_id():
    url = "http://91.210.171.73:8080/api/category/1"  # Замените 1 на реальный ID категории
    auth = ('admin', 'admin')

    response = requests.get(url, auth=auth)

    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.headers["Content-Type"] == "application/json", "Expected JSON response"

    json_data = response.json()
    assert "id" in json_data
    assert "name" in json_data

def test_update_category():
    url = "http://91.210.171.73:8080/api/category/1"  # Замените 1 на реальный ID категории
    auth = ('admin', 'admin')

    payload = {
        "id": 1,
        "name": "Updated Category Name"
    }

    response = requests.put(url, json=payload, auth=auth)

    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.headers["Content-Type"] == "application/json", "Expected JSON response"

    json_data = response.json()
    assert "id" in json_data
    assert "name" in json_data

    assert json_data["id"] == payload["id"]
    assert json_data["name"] == payload["name"]

def test_delete_category():
    url = "http://91.210.171.73:8080/api/category/1"  # Замените 1 на реальный ID категории
    auth = ('admin', 'admin')

    response = requests.delete(url, auth=auth)

    assert response.status_code == 204, f"Expected status code 204, but got {response.status_code}"


 

def test_get_pets():
    url = "http://91.210.171.73:8080/api/pet/"
    auth = ('admin', 'admin')

    response = requests.get(url, auth=auth)

    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.headers["Content-Type"] == "application/json", "Expected JSON response"

    json_data = response.json()
    assert "count" in json_data
    assert "next" in json_data
    assert "previous" in json_data
    assert "results" in json_data
    assert len(json_data["results"]) > 0, "Expected non-empty list of pets"

def test_create_pet():
    url = "http://91.210.171.73:8080/api/pet/"
    auth = ('admin', 'admin')
    data = {
        "name": "Fluffy",
        "photo_url": "http://example.com/fluffy.jpg",
        "category": {
            "id": 1,
            "name": "Cat"
        },
        "status": "available"
    }

    response = requests.post(url, json=data, auth=auth)

    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
    assert response.headers["Content-Type"] == "application/json", "Expected JSON response"

    json_data = response.json()
    assert "id" in json_data
    assert json_data["name"] == "Fluffy"
    assert json_data["photo_url"] == "http://example.com/fluffy.jpg"
    assert json_data["category"]["id"] == 1
    assert json_data["status"] == "available"

def test_get_pet_by_id():
    pet_id = 1
    url = f"http://91.210.171.73:8080/api/pet/{pet_id}/"
    auth = ('admin', 'admin')

    response = requests.get(url, auth=auth)

    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.headers["Content-Type"] == "application/json", "Expected JSON response"

    json_data = response.json()
    assert "id" in json_data
    assert json_data["id"] == pet_id

def test_update_pet():
    pet_id = 1
    url = f"http://91.210.171.73:8080/api/pet/{pet_id}/"
    auth = ('admin', 'admin')
    data = {
        "name": "Fluffy Updated",
        "photo_url": "http://example.com/fluffy_updated.jpg",
        "category": {
            "id": 1,
            "name": "Cat"
        },
        "status": "available"
    }

    response = requests.put(url, json=data, auth=auth)

    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.headers["Content-Type"] == "application/json", "Expected JSON response"

    json_data = response.json()
    assert "id" in json_data
    assert json_data["id"] == pet_id
    assert json_data["name"] == "Fluffy Updated"
    assert json_data["photo_url"] == "http://example.com/fluffy_updated.jpg"
    assert json_data["category"]["id"] == 1
    assert json_data["status"] == "available"

def test_delete_pet():
    pet_id = 1
    url = f"http://91.210.171.73:8080/api/pet/{pet_id}/"
    auth = ('admin', 'admin')

    response = requests.delete(url, auth=auth) 

    assert response.status_code == 204, f"Expected status code 204, but got {response.status_code}"
