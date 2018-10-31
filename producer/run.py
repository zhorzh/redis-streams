from walrus import Database  # A subclass of the redis-py Redis client.
import time

db = Database(host='redis', port=6379, db=0)
stream = db.Stream('twitter')

for n in range(10):
    message = {'text': 'TEXT MESSAGE #{}'.format(n)}
    msgid = stream.add(message)
    print(message['text'])
    time.sleep(1)
