import requests

def client():

    # data = {
    #     'username': 'testrest5', 
    #     'email': 'test5@rest.com',
    #     'password1':'aaaaaa100',
    #     'password2':'aaaaaa100'
    #     }
    # response = requests.post('http://127.0.0.1:8000/api/rest-auth/registration/', data=data)

    token_header = 'Token 1e79d303502356aba4a8e5bcda427b2f48404793'
    headers = {"Authorization": token_header}
    response = requests.get('http://127.0.0.1:8000/api/profiles/', headers=headers)

    print(f"Status code: {response.status_code}")
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()