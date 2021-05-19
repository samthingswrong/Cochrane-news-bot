from os import environ


API_TOKEN = '1538451446:AAGPDqowCQ6cWhbcxCb8GxYSFV0nahBwUMU' #environ['API_KEY']

DATABASE_URL = 'postgres://nvjayddvjkefcv:d85f43de202d4090d7f9089cdf6c998f0aef29d7a518e7b2349b490b50f54998@ec2-34-240-75-196.eu-west-1.compute.amazonaws.com:5432/dagihpa0k8dsn7'#environ['DATABASE_URL']
HOST = 'ec2-34-240-75-196.eu-west-1.compute.amazonaws.com'#environ['HOST']
DB_NAME = 'dagihpa0k8dsn7' #environ['DB_NAME']
USER_NAME = 'nvjayddvjkefcv'#environ['USER_NAME']
PASSWORD = 'd85f43de202d4090d7f9089cdf6c998f0aef29d7a518e7b2349b490b50f54998'#environ['PASSWORD']


commands = ['/help - open command list',
            '/news - get latest news and events',
            '/sub - subscribe to the newsletter',
            '/unsub - cancel subscription',
            '/top_news X - get last X[1-8] posts',
            '/top_evidence X - get topX[1-10] posts']
