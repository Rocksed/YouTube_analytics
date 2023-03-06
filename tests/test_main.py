import pytest
from utils.main import Video, PLVideo


# test Video class
def test_video_init():
    video = Video('9lO06Zxhu88')
    assert video.video_id == '9lO06Zxhu88'
    assert isinstance(video.title, str)
    assert isinstance(video.views, int)
    assert isinstance(video.likes, int)


# test PLVideo class
def test_plvideo_init():
    plvideo = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
    assert plvideo.video_id == 'BBotskuyw_M'
    assert plvideo.playlist_id == 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD'
    assert isinstance(plvideo.title, str)
    assert isinstance(plvideo.views, int)
    assert isinstance(plvideo.likes, int)
    assert isinstance(plvideo.playlist_name, str)


# test Video and PLVideo __str__() methods
def test_video_str():
    video = Video('9lO06Zxhu88')
    assert str(video) == "Как устроена IT-столица мира / Russian Silicon Valley (English subs)"


def test_plvideo_str():
    plvideo = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
    assert str(plvideo) == "Пушкин: наше все? (Литература)"
