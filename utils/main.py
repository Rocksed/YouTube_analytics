import requests
import json


class Channel:
    def __init__(self, id):
        self.id = id
        self.name = ''
        self.description = ''
        self.views = 0
        self.subscribers = 0
        self.get_data()

    def get_data(self):
        api_key = 'your API key should be here'
        url = f'https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={self.id}&key={api_key}'
        response = requests.get(url)
        data = json.loads(response.text)['items'][0]

        self.name = data['snippet']['title']
        self.description = data['snippet']['description']
        self.views = int(data['statistics']['viewCount'])
        self.subscribers = int(data['statistics']['subscriberCount'])

    def print_info(self):
        print(f'Name: {self.name}')
        print(f'Description: {self.description}')
        print(f'Views: {self.views}')
        print(f'Subscribers: {self.subscribers}')


vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
vdud.print_info()
