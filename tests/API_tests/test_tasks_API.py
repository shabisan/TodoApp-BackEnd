import requests

url = "http://localhost:8081/api/v1/tasks"

response = requests.get(url=url)
expected_status = 403
expected_data_key = "message"
expected_data_value = "Missing token"


if __name__ == '__main__':
    status = response.status_code
    data = response.json()

    assert status == expected_status
    for key, value in data.items():
        assert key == expected_data_key
        assert value == expected_data_value

    print(response)
