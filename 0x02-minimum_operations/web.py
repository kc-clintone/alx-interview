#!/usr/bin/env python3
"""
Module for fetching and caching web pages.
"""

import requests
import redis
from functools import wraps
from typing import Callable


redis_client = redis.Redis()


def cache_with_expiration(expiration: int):
    """
    Decorator to cache the result of a function in Redis
    with a specified expiration time.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(url: str) -> str:
            cached_result = redis_client.get(f"cached:{url}")
            if cached_result:
                return cached_result.decode('utf-8')

            result = func(url)
            redis_client.setex(f"cached:{url}", expiration, result)
            return result

        return wrapper
    return decorator


@cache_with_expiration(10)
def get_page(url: str) -> str:
    """
    Fetches the HTML content of a URL and caches the result.
    Tracks the number of times the URL was accessed.
    """
    redis_client.incr(f"count:{url}")

    response = requests.get(url)
    return response.text
