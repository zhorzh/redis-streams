from walrus import Database  # A subclass of the redis-py Redis client.
# import time

db = Database(host='redis', port=6379, db=0)
stream = db.Stream('twitter')

while True:
    response = stream.read(timeout=100, last_id='$')
    if response:
        timestamp, message = response[0]
        print(message[b'text'])
