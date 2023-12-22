import requests

base_url = 'https://api-uc.wallpaperscraft.com/images'
query = input('What do you want to search?: ')
params = {
    'limit': 15,
    'query': query,
    'screen[height]': 2556,
    'screen[width]': 1179,
    'sort': 'rating'
}

response = requests.get(base_url, params=params).json()
for url in response['items']:
    print('URL:', url['variations']['adapted']['url'])
