import requests


if __name__ == '__main__':
    URL = "http://localhost:8081/api/v1/users/sign-in"
    user = {"name": "Sigalit", "email": "t4@t.aaa", "password": "maya"}
    response = requests.post(URL, json=user)
    x = response.headers.get("Authorization")


    URL = "http://localhost:8081/api/v1/users/login"
    credentials = {"email": "t4@t.aaa", "password": "maya"}
    response = requests.post(URL, json=credentials)
    y = response.headers.get("Authorization")

    assert x == y, "f/Toekns are not equal"


