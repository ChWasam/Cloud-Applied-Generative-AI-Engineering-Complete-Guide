# Problem3: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.

#  Matlab kya aus sa ho kah gya ha ausa pta ha imediately (Yeh buhat hi amazing feature ha )
import time
def cache(func):
    cache_value = {}
    def wrapper(*args,**kwargs):
        if args in cache_value:
            return cache_value[args]
        result =func(*args,**kwargs)
        cache_value[args] = result
        return result
    return wrapper

@cache
def any_function(num1,num2):
    time.sleep(4)
    return num1+num2

print(any_function(2,3))
print(any_function(2,3))
print(any_function(2,3))

# import time

# def cache(func):
#     cache_value = {}
#     def wrapper(*args):
#         if args in cache_value:
#             return cache_value[args]
#         result = func(*args)
#         cache_value[args] = result
#         return result
#     return wrapper

# @cache
# def long_running_function(a, b):
#     time.sleep(4)
#     return a + b

# print(long_running_function(2, 3))
# print(long_running_function(2, 3))
# print(long_running_function(2, 3))
# print(long_running_function(4, 3))
# print(long_running_function(2, 3))




# print({(2,3):5})


 






