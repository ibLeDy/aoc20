import contextlib
import time


# stolen from @anthonywritescode's support module
# https://github.com/anthonywritescode/aoc2020
@contextlib.contextmanager
def timing(name=''):
    before = time.time()
    try:
        yield
    finally:
        after = time.time()
        t = (after - before) * 1000
        unit = 'ms'
        if t < 100:
            t *= 1000
            unit = 'μs'
        if name:
            name = f' ({name})'
        print(f'> {int(t)} {unit}{name}')
