import requests

url = "http://localhost:8081/api/v1/todos"

if __name__ == '__main__':
    response = requests.get(url=url)
    headers = response.headers
    data = response.json()


