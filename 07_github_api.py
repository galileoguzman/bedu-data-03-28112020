import requests

# CONSTANTS
BASE_URL = 'https://api.github.com/'

# FUNCTIONS
def get_github_user(username):
    url = f'{BASE_URL}users/{username}'
    respose = requests.get(url)
    if respose.status_code == 200:
        return respose.json()
    return None


username = input('Give me a Github username:\t')
user = get_github_user(username)
print(user)
