import requests

url = "http://localhost:8081/api/v1/status"

# response = requests.get(url=url)
# expected_status = 200
# expected_keys = ["status", "timestamp"]
# expected_status_value = "test"
if __name__ == '__main__':
    url = "http://localhost:8081/api/v1/users/login"
    credentials = {"email": "alef.bet@todo.com", "password": "Aa123456"}
    response = requests.post(url, json=credentials)
    token = response.headers.get("Authorization")
    header = {"Authorization":token}
    url = "http://localhost:8081/api/v1/tasks"
    status = response.status_code
    data = response.json()
    actual_url = response.url

    assert actual_url == url
    assert status == expected_status
    for key,value in data.items():
        assert key in expected_keys
    assert data["status"] == expected_status_value


    print(status)
    print(data)
    print(actual_url)

