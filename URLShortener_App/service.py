import secrets
import string
from django.core.cache import cache

def generate_short_url():
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(6))



def click_count(short_url):
    redis_key=f"clicks:{short_url}"
    try:
        cache.incr(redis_key)
    except ValueError:
        cache.set(redis_key,1)