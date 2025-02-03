import requests

# Substitua pelo seu token de acesso pessoal
GITHUB_TOKEN = 'seu_token_aqui'
HEADERS = {'Authorization': f'token {GITHUB_TOKEN}'}

def get_following(username):
    following = []
    url = f'https://api.github.com/users/{username}/following'
    while url:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            following.extend([user['login'] for user in response.json()])
            url = response.links.get('next', {}).get('url')
        else:
            print(f"Erro ao obter seguindo: {response.status_code}")
            break
    return following

def get_followers(username):
    followers = []
    url = f'https://api.github.com/users/{username}/followers'
    while url:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            followers.extend([user['login'] for user in response.json()])
            url = response.links.get('next', {}).get('url')
        else:
            print(f"Erro ao obter seguidores: {response.status_code}")
            break
    return followers

def find_non_followers(username):
    following = get_following(username)
    followers = get_followers(username)
    
    non_followers = [user for user in following if user not in followers]
    
    return non_followers

if __name__ == "__main__":
    username = 'seu_username_github'  # Substitua pelo seu username do GitHub
    non_followers = find_non_followers(username)
    
    if non_followers:
        print("Pessoas que você segue, mas não seguem você de volta:")
        for user in non_followers:
            print(user)
    else:
        print("Todos que você segue também te seguem de volta!")