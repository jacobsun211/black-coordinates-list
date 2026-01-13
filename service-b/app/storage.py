from fastapi import FastAPI, APIRouter
import redis
from pydantic import BaseModel



redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)
# see what keys are in Redis

# print(redis_db.set('half stack', 'java'))  # adds "full stack":'python' to redis db
# print(redis_db.keys())                       # get all keys
# key = redis_db.get('half stack')   # get spesific value based on key
# print(redis_db.incr('data'))    # inc and create if not exist


def get_coord():
    all_data = {}
    for keys in redis_db.keys():
        values = redis_db.get(keys)
        key = keys.decode()     
        value = values.decode() 
        all_data[key] = value
    return all_data


def post_coord(ip, coord):
    redis_db.set(ip,coord)  
    return True






