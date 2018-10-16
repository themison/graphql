import random

def secret():
    hash = random.sample('123456789qwertyuiopasdfghjklzxcvbnm', 10)
    str = ''.join(hash)
    return str