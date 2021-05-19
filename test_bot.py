import unittest
import parser as prs


class TestBot(unittest.TestCase):
    def test_get_ok(self):
        self.assertEqual(prs.get_html(prs.NEWS_URL).ok, True)

    def test_last_post_key_init(self):
        pr = prs.NewsParser()
        self.assertEqual(pr.get_last_post_key(), 0)

