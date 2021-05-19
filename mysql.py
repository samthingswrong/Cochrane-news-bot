import psycopg2
import config as cfg


class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            host=cfg.HOST,
            dbname=cfg.DB_NAME,
            user=cfg.USER_NAME,
            password=cfg.PASSWORD)
        self.cur = self.connection.cursor()

    # Create users table
    def create_table(self):
        with self.connection:
            self.cur.execute("CREATE TABLE users (user_id integer, sub_status smallint); ")

    # Get list of users with certain status (True by default)
    def get_users(self, sub_status=1):
        with self.connection:
            return self.cur.execute(""" SELECT * FROM users WHERE sub_status = ?;""",
                                    (sub_status,)).fetchall()

    # Check user existence
    def user_exists(self, user_id):
        with self.connection:
            result = self.cur.execute(""" SELECT * FROM users WHERE user_id = ?;""",
                                      (user_id,)).fetchall()
            return bool(len(result))

    # Add new user to database
    def add_user(self, user_id, sub_status=1):
        with self.connection:
            return self.cur.execute(""" INSERT INTO users (user_id, sub_status) VALUES(?,?);""",
                                    (user_id, sub_status))

    # Make existing user a subscriber
    def update_subscription(self, user_id, sub_status):
        with self.connection:
            return self.cur.execute(""" UPDATE users SET sub_status = ? WHERE user_id = ?;""",
                                    (sub_status, user_id))

    # Remove user from database
    def remove_user(self, user_id):
        with self.connection:
            return self.cur.execute(""" DELETE FROM users WHERE user_id = ?;""",
                                    (user_id,))

    # Close connection with database
    def close(self):
        self.cur.close()
        self.connection.close()
