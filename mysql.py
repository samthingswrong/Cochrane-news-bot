import psycopg2


class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            host="ec2-54-155-208-5.eu-west-1.compute.amazonaws.com",
            database="d6njl67qe4of0h",
            user="thpkcrtlyjbol",
            password="2c398e922a079211293dac6fb93b158fa89feee676388e422668a204bdd4890f")
        self.cur = self.connection.cursor()

    # Create users table
    def create_table(self):
        with self.connection:
            self.cur.execute("""CREATE TABLE `users` (user_id, sub_status)""")

    # Get list of users with certain status (True by default)
    def get_users(self, sub_status=1):
        with self.connection:
            return self.cur.execute(""" SELECT * FROM `users` WHERE `sub_status` = ? """,
                                    (sub_status,)).fetchall()

    # Check user existence
    def user_exists(self, user_id):
        with self.connection:
            result = self.cur.execute(""" SELECT * FROM `users` WHERE `user_id` = ? """,
                                      (user_id,)).fetchall()
            return bool(len(result))

    # Add new user to database
    def add_user(self, user_id, sub_status=1):
        with self.connection:
            return self.cur.execute(""" INSERT INTO `users` (`user_id`, `sub_status`) VALUES(?,?) """,
                                    (user_id, sub_status))

    # Make existing user a subscriber
    def update_subscription(self, user_id, sub_status):
        with self.connection:
            return self.cur.execute(""" UPDATE `users` SET `sub_status` = ? WHERE `user_id` = ? """,
                                    (sub_status, user_id))

    # Remove user from database
    def remove_user(self, user_id):
        with self.connection:
            return self.cur.execute(""" DELETE FROM `users` WHERE `user_id` = ?""",
                                    (user_id,))

    # Close connection with database
    def close(self):
        self.connection.close()
