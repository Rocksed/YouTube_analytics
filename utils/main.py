import os
from googleapiclient.discovery import build
from dotenv import load_dotenv


class Video:
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'

    def __init__(self, video_id):
        self._id = video_id
        self._title = None
        self._view_count = None
        self._like_count = None
        self._get_data()

    @staticmethod
    def get_service():
        load_dotenv()
        api_key = os.getenv('YOUTUBE_API_KEY')
        return build(Video.YOUTUBE_API_SERVICE_NAME, Video.YOUTUBE_API_VERSION, developerKey=api_key)

    def _get_data(self):
        youtube = Video.get_service()
        response = youtube.videos().list(
            part='snippet,statistics',
            id=self._id
        ).execute()
        if response.get('items'):
            data = response['items'][0]
            self._title = data['snippet']['title']
            self._view_count = int(data['statistics']['viewCount'])
            self._like_count = int(data['statistics']['likeCount'])
        else:
            raise ValueError(f"No video data found for video ID {self._id}")

    @property
    def title(self):
        return self._title

    @property
    def view_count(self):
        return self._view_count

    @property
    def like_count(self):
        return self._like_count

    def __str__(self):
        return f"{self._title}"

    def __repr__(self):
        return f"Video('{self._id}')"


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        self._playlist_name = None
        self._playlist_id = playlist_id
        super().__init__(video_id)

    def _get_data(self):
        super()._get_data()
        youtube = Video.get_service()
        response = youtube.playlists().list(
            part='snippet',
            id=self._playlist_id
        ).execute()
        if response.get('items'):
            data = response['items'][0]
            self._playlist_name = data['snippet']['title']
        else:
            raise ValueError(f"No playlist data found for playlist ID {self._playlist_id}")

    @property
    def playlist_name(self):
        return self._playlist_name

    def __str__(self):
        return f"{self._title} ({self._playlist_name})"

    def __repr__(self):
        return f"PLVideo('{self._id}', '{self._playlist_id}')"


video1 = Video('9lO06Zxhu88')
video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
print(video1)
print(video2)
