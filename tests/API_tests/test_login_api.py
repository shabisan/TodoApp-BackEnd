import requests

expected_values = ["Login Successfully!", "success"]

if __name__ == '__main__':

    url = "http://localhost:8081/api/v1/users/login"
    credentials = {"email": "alef.bet@todo.com", "password": "Aa123456"}
    response = requests.post(url, json=credentials)
    headers = response.headers
    data = response.json()
    actual_url = response.url
    status = response.status_code
    assert actual_url == url
    for key,value in data.items():
        if key == "timestamp":
            continue
        assert value in expected_values
    print(headers)
    print(data)


