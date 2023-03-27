import os
from datetime import timedelta
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
        self._duration = None
        self._get_data()

    @staticmethod
    def get_service():
        load_dotenv()
        api_key = os.getenv('YOUTUBE_API_KEY')
        return build(Video.YOUTUBE_API_SERVICE_NAME, Video.YOUTUBE_API_VERSION, developerKey=api_key)

    def _get_data(self):
        youtube = Video.get_service()
        response = youtube.videos().list(
            part='snippet,statistics,contentDetails',
            id=self._id
        ).execute()
        if response.get('items'):
            data = response['items'][0]
            self._title = data['snippet']['title']
            self._view_count = int(data['statistics']['viewCount'])
            self._like_count = int(data['statistics']['likeCount'])
            duration_str = data['contentDetails']['duration']
            self._duration = timedelta(seconds=Video.parse_duration(duration_str))
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

    @property
    def duration(self):
        return self._duration

    @staticmethod
    def parse_duration(duration_str):
        parts = duration_str.replace('PT', '').split('H')
        time_parts = [int(p.strip('M').strip('S')) for p in parts[-1].split('M')]
        if len(parts) > 1:
            time_parts.insert(0, int(parts[0]))
        return sum([tp * (60 ** i) for i, tp in enumerate(reversed(time_parts))])

    def __str__(self):
        return f"{self._title}"

    def __repr__(self):
        return f"Video('{self._id}')"


class PlayList:
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'

    def __init__(self, playlist_id):
        self._id = playlist_id
        self._title = None
        self._videos = []
        self._get_data()

    @staticmethod
    def get_service():
        load_dotenv()
        api_key = os.getenv('YOUTUBE_API_KEY')
        return build(PlayList.YOUTUBE_API_SERVICE_NAME, PlayList.YOUTUBE_API_VERSION, developerKey=api_key)

    def _get_data(self):
        youtube = PlayList.get_service()
        response = youtube.playlists().list(
            part='snippet',
            id=self._id
        ).execute()
        if response.get('items'):
            data = response['items'][0]
            self._title = data['snippet']['title']
            nextPageToken = None
            while True:
                pl_response = youtube.playlistItems().list(
                    part="snippet",
                    playlistId=self._id,
                    maxResults=50,
                    pageToken=nextPageToken
                ).execute()
                self._videos.extend([Video(item['snippet']['resourceId']['videoId']) for item in pl_response['items']])
                nextPageToken = pl_response.get('nextPageToken')
                if not nextPageToken:
                    break

    @property
    def title(self):
        return self._title

    @property
    def videos(self):
        return self._videos

    @property
    def url(self):
        return f"https://www.youtube.com/playlist?list={self._id}"

    def __str__(self):
        return f"{self._title}"

    def __repr__(self):
        return f"PlayList('{self._id}')"

    @property
    def total_duration(self):
        total_duration = sum([v.duration for v in self._videos], timedelta())
        return total_duration

    def show_best_video(self):
        best_video = max(self._videos, key=lambda v: v.view_count)
        return best_video


pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')

print(pl.title)
print(pl.url)

duration = pl.total_duration
print(duration)
print(type(duration))
print(duration.total_seconds())

print(pl.show_best_video())
