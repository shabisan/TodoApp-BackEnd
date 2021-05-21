import requests

expected_keys = ["message"]

if __name__ == '__main__':
    url = "http://localhost:8081/api/v1/users/login"
    credentials = {"email": "alef.bet@todo.com", "password": "Aa123456"}
    response = requests.post(url, json=credentials)
    token = response.headers.get("Authorization")
    header = {"Authorization":token}
    url = "http://localhost:8081/api/v1/tasks"
    task = {"taskDescription": "furnish the living room"}
    response = requests.post(url, json=task, headers=header)
    headers = response.headers
    data = response.json()
    actual_url = response.url
