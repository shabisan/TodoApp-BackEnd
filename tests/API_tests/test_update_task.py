import json

import requests


if __name__ == '__main__':
    '''
    Step 1 - Login to Server 
    '''
    url = "http://localhost:8081/api/v1/users/login"
    credentials = {"email": "alef.bet@todo.com", "password": "Aa123456"}
    response = requests.post(url, json=credentials)
    token = response.headers.get("Authorization")
    header = {"Authorization":token}
    '''
    Step 2 - From Tasks - Retrieve Tadk_ID (Should be in data)
    '''
    url = "http://localhost:8081/api/v1/tasks"
    task = {"taskDescription": "furnish the living room"}
    response = requests.get(url, json=task, headers=header)
    status = response.status_code
    data = response.json()
    '''
    step 3 - access Task with task_ID  from "data" field and make the required changes)
    '''
    TID = data['data'][1]['taskId']
    url = "http://localhost:8081/api/v1/tasks/" + TID
    payload = {"taskDescription": "furnish the living room",  "isCompleted": "True"}
    response = requests.put(url,json=payload, headers=header)
    status = response.status_code
    data = response.json()



    # print(status)
    # print(data)

