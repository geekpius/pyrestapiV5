import requests

def client():
    # credentials = {'username': 'admin', 'password':'aaaaaa'}
    # response = requests.post('http://127.0.0.1:8000/api/rest-auth/login/', data=credentials)
    token_header = 'Token eae25968584ec411f76f04be04a11cffd80f886e'
    headers = {"Authorization": token_header}
    response = requests.get('http://127.0.0.1:8000/api/profiles/', headers=headers)

    print(f"Status code: {response.status_code}")
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()