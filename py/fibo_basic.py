def fib(n):

    result = []

    a = 0
    b = 1

    for i in range(n):
        a, b = b, a+b
        result.append(b)
    return result    



def fib_recursive(n):

    if n < 2:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

cache = dict()
def fib_recursive_memo(n):
    if n < 2:
        return n
    
    if n in cache:
        return cache[n]
    else:
        cache[n] = fib_recursive_memo(n-1) + fib_recursive_memo(n-2)

    return cache[n]


fib_results = fib(10)
print(fib_results)

print(fib_recursive(10))

print(fib_recursive_memo(11))

print('hi')