import time
from functools import wraps

def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func) # @wraps(func) 能保留原始函数的元数据
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

# use
@timethis
def countdown(n):
    '''
    Counts down
    '''
    while n > 0:
        n -= 1

# >>> countdown.__name__
# 'countdown'
# >>> countdown.__doc__
# '\n\tCounts down\n\t'
# >>> countdown.__annotations__
# {'n': <class 'int'>}
# >>>
from inspect import signature
print(signature(countdown))
# 使用 countdown.__wrapped__ 访问原始函数
# 如果有多个包装器，那么访问 __wrapped__ 属性的行为是不可预知的，应该避免这样做。
