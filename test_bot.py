import unittest
import parser as pr


class TestBot(unittest.TestCase):
    def test_get_ok(self):
        self.assertEqual(pr.get_html(pr.NEWS_URL).ok, True)

    def test_last_post_key_init(self):
        prs = pr.NewsParser()
        self.assertEqual(prs.get_last_post_key(), 0)

    def test_new_post_key(self):
        prs = pr.NewsParser()
        self.assertEqual(prs.get_new_post_key(), 71054)
