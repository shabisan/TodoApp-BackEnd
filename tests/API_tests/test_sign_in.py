import requests

expected_keys = ["status", "timestamp"]

if __name__ == '__main__':

    url = "http://localhost:8081/api/v1/users/sign-in"
    credentials = {"name": "shabisan2","email": "dalet.hey@todo.com", "password": "Aa123456"}
    response = requests.post(url, json=credentials)
    headers = response.headers
    data = response.json()
    actual_url = response.url
    assert actual_url == url
    for key,value in data.items():
        assert key in expected_keys
    print(headers)
    print(data)
