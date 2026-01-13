print("hello world")
redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)
# see what keys are in Redis

print(redis_db.set('half stack', 'java'))  # adds "full stack":'python' to redis db
print(redis_db.keys())                       # get all keys
key = redis_db.get('half stack')   # get spesific value based on key
print(redis_db.incr('data'))    # inc and create if not exist

key = key[0:]
print(key)

print(redis_db.delete('twilio'))    # delete the key:value based on key
