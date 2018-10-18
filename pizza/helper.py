from django.utils.crypto import get_random_string

def secret():
    hash = get_random_string(length=10)
    return hash