import unittest
import sqlite3

from random import randrange

import mysql
import parser as prs


class TestBot(unittest.TestCase):
    def test_get_ok(self):
        self.assertEqual(prs.get_html(prs.NEWS_URL).ok, True)

    def test_last_post_key_init(self):
        pr = prs.NewsParser()
        self.assertEqual(pr.get_last_post_key(), 0)

    def test_add_user_to_db(self):
        test_id = randrange(100000)
        db = mysql.Database("db/users.db")
        db.add_user(test_id)
        users = db.get_users()
        self.assertEqual(users[len(users) - 1][0], test_id)
        db.remove_user(test_id)
        db.close()
