import redis

# התחברות ל-Redis עם הכתובת "redis" בקונטיינר של Docker
redis_con = redis.StrictRedis(host="redis", port=6379, db=0, decode_responses=True)

# פונקציה להמיר את המידע מ-Redis (אם הוא מוצג כ-BYTES) למחרוזות
def convertor(data):
    if isinstance(data, bytes):
        return data.decode('utf-8')
    elif isinstance(data, dict):
        return {key.decode('utf-8'): value.decode('utf-8') for key, value in data.items()}
    elif isinstance(data, list):
        return [item.decode('utf-8') for item in data]
    return data
