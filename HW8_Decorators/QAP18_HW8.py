# 1 Написать обычную функцию для факториала, генератор и рекурсию. Сравнить их время работы

import timeit


def factorial_simple(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


def factorial_generator(m):
    res = 1
    for i in range(2, m + 1):
        res *= i
        yield res


def factorial_recursive(i):
    if i == 0:
        return 1
    else:
        return n * factorial_recursive(i - 1)


def compare_factorial_methods(n):
    # Simple function timing
    simple_time = timeit.timeit(lambda: factorial_simple(n), number=1000)

    # Generator method timing
    generator_time = timeit.timeit(lambda: list(factorial_generator(n))[-1], number=1000)

    # Recoursive method timing
    recursive_time = timeit.timeit(lambda: factorial_recursive(n), number=1000)

    return simple_time, generator_time, recursive_time


n = 10
simple_time, generator_time, recursive_time = compare_factorial_methods(n)
print(f"Simple method time: {simple_time:.6f} seconds")
print(f"Generator method time: {generator_time:.6f} seconds")
print(f"Recursive method time: {recursive_time:.6f} seconds")

# 2 Напишите декоратор, который проверял бы тип параметров функции, конвертировал их если надо и складывал:


def typed(type):
    def decorator(function):
        def wrapper(*args):
            new_args = []
            for i in args:
                if isinstance(i, type):
                    new_args.append(i)
                else:
                    new_args.append(type(i))
            return function(*new_args)
        return wrapper
    return decorator


@typed(str)
def add_two_symbols(a, b):
    return a + b


print(add_two_symbols("3", 5))
print(add_two_symbols(5, 5))
print(add_two_symbols('a', 'b'))


@typed(int)
def add_three_symbols(a, b, с):
    return a + b + с


print(add_three_symbols(5, 6, 7))
print(add_three_symbols("3", 5, 0))
print(add_three_symbols(0.1, 0.2, 0.4))
