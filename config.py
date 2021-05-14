from os import environ


API_TOKEN = environ['API_KEY']

commands = ['/help - open command list',
            '/news - get latest news and events',
            '/sub - subscribe to the newsletter',
            '/unsub - cancel subscription',
            '/top_news X - get last X[1-8] posts',
            '/top_evidence X - get topX[1-10] posts']
