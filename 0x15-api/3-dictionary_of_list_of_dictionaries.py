#!/usr/bin/python3
"""Python script that, using this REST API, ,
returns information about all users 'TODO' list progress.
and export data in the JSON format."""

import requests
"""  Importing modules """


def get_employee_todo_progress():
    """ get_employee_todo_progress """

    url = f"https://jsonplaceholder.typicode.com/users/"
    users_response = requests.get(f'{url}')
    if users_response.status_code != 200:
        print(f"Failed to retrieve data.")
        return
    users_data = users_response.json()
    all_id = []
    for user in users_data:
        all_id.append(user["id"])
    datav1 = "{"
    for EmpID in all_id:
        url1 = f"https://jsonplaceholder.typicode.com/users/{EmpID}"
        user_resp = requests.get(f'{url1}')
        url2 = f'https://jsonplaceholder.typicode.com/todos?userId={EmpID}'
        todos_resp = requests.get(f'{url2}')
        if user_resp.status_code != 200 or todos_resp.status_code != 200:
            print(f"Failed to retrieve data. Check if the employee ID .")
            return
        user_data = user_resp.json()
        todos_data = todos_resp.json()
        emp = user_data['username']
        data = f'"{EmpID}": ['
        for todo in todos_data:
            st = str(todo['completed']).lower()
            tl = todo['title']
            data += "{"
            data += f'"username": "{emp}", "task": "{tl}", "completed": {st}'
            data += "}, "
        content = data.rstrip(", ")
        content += "], "
        datav1 += content
    AllUsersData = datav1.rstrip(", ")
    AllUsersData += "}"

    json_file = "todo_all_employees.json"
    with open(json_file, 'w') as file:
        file.write(AllUsersData)


if __name__ == "__main__":
    get_employee_todo_progress()
