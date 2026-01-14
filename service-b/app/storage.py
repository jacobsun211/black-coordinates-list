import redis

redis_db = redis.StrictRedis(host="redis", port=6379, db=0)


def get_coord():
    all_data = {}
    for keys in redis_db.keys():
        values = redis_db.get(keys)
        key = keys.decode()
        value = values.decode()
        all_data[key] = value
    return all_data


def post_coord(ip, coord):
    redis_db.set(ip, coord)
    return True
