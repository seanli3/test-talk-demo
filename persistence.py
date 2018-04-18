from redis import StrictRedis

r = StrictRedis(host='localhost', port=6379, db=0)

def add_bmi(bmi):
    r.lpush('bmi', bmi)

def get_bmi_list():
    return [float(x) for x in r.lrange("bmi", 0, -1)]
