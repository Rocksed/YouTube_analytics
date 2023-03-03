import unittest
from utils.main import Channel


class TestChannel(unittest.TestCase):

    def setUp(self):
        self.ch1 = Channel('UC-lHJZR3Gqxm24_Vd_AJ5Yw')  # PewDiePie's channel ID
        self.ch2 = Channel('UCiDJtJKMICpb9B1qf7qjEOA')  # T-Series' channel ID

    def test_channel_info(self):
        self.assertEqual(self.ch1.channel_id, 'UC-lHJZR3Gqxm24_Vd_AJ5Yw')
        self.assertEqual(self.ch1.title, 'PewDiePie')
        self.assertEqual(self.ch1.description, 'I make videos.')
        self.assertEqual(self.ch1.url, 'https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw')
        self.assertGreater(self.ch1.subscriber_count, 100000)
        self.assertGreater(self.ch1.video_count, 1000)
        self.assertGreater(self.ch1.view_count, 10000000)

    def test_channel_print(self):
        self.assertEqual(str(self.ch1), 'Youtube-channel: PewDiePie')

    def test_channel_addition(self):
        total_subscribers = self.ch1.subscriber_count + self.ch2.subscriber_count
        self.assertEqual(self.ch1 + self.ch2, total_subscribers)

    def test_channel_comparison(self):
        self.assertGreater(self.ch1, self.ch2)
        self.assertLess(self.ch2, self.ch1)


if __name__ == '__main__':
    unittest.main()
