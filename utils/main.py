import json
import os

from googleapiclient.discovery import build


class Channel:
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'

    def __init__(self, channel_id):
        self._id = channel_id
        self._title = None
        self._description = None
        self._url = None
        self._subscriber_count = None
        self._video_count = None
        self._view_count = None
        self._get_data()

    @staticmethod
    def get_service():
        api_key = 'your API'
        return build(Channel.YOUTUBE_API_SERVICE_NAME, Channel.YOUTUBE_API_VERSION, developerKey=api_key)

    @property
    def channel_id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def url(self):
        return self._url

    @property
    def subscriber_count(self):
        return self._subscriber_count

    @property
    def video_count(self):
        return self._video_count

    @property
    def view_count(self):
        return self._view_count

    def _get_data(self):
        youtube = Channel.get_service()
        response = youtube.channels().list(
            part='snippet,statistics',
            id=self._id
        ).execute()
        data = response['items'][0]

        self._title = data['snippet']['title']
        self._description = data['snippet']['description']
        self._url = f"https://www.youtube.com/channel/{self._id}"
        self._subscriber_count = int(data['statistics']['subscriberCount'])
        self._video_count = int(data['statistics']['videoCount'])
        self._view_count = int(data['statistics']['viewCount'])

    def to_json(self, filename):
        data = {
            'channel_id': self._id,
            'title': self._title,
            'description': self._description,
            'url': self._url,
            'subscriber_count': self._subscriber_count,
            'video_count': self._video_count,
            'view_count': self._view_count
        }

        with open(filename, 'w') as file:
            json.dump(data, file)

        print(f"Data saved to {os.path.abspath(filename)}")


vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')

# get attribute values
print(vdud.title)
print(vdud.video_count)
print(vdud.url)

# can't change
# vdud.channel_id = 'New name'  # raises AttributeError

# can get the object for working with API outside the class
print(Channel.get_service())

# create a 'vdud.json' file with channel data
vdud.to_json('vdud.json')
