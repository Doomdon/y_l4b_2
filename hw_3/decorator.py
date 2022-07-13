import functools
import logging

logging.basicConfig()
_LOGGING_LEVEL = logging.DEBUG
_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(_LOGGING_LEVEL)


def cached(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):

        # signature = (func, args)
        _LOGGER.debug('using signature')

        if args in cache:

            _LOGGER.debug('retrieving from cache')
            result = cache[args]

        else:
            # _LOGGER.debug('retrieving from cache: %s', signature)
            result = func(*args)
            _LOGGER.debug('сaching: %s', result)
            cache[args] = result

        return result

    return wrapper


@cached
def multiplier(number: int):
    return number * 2


# тесты
def tests():
    print(multiplier(2))
    print(multiplier(2))
    print(multiplier(2))
    print(multiplier(str(2)))
    a = {1: 3,
         2: 3,
         'key': 'value'}
    print(multiplier(str(a)))
    print(multiplier(str(a)))
    print(multiplier(str(a)))


if __name__ == "__main__":
    tests()
