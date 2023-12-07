# Задание №1
# Написать декоратор, который оборачивает строку в теги <i></i>.
import math

def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'<i>{result}</i>'
    return wrapper

@decorator
def decorate_text(text):
    return text

def decorator1(func):
    def obertka(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'<strong>{result}</strong>'
    return obertka

@decorator1
def decorate_text1_v1(text):
    return text

def decorator12(func):
    def obertka(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'<strong>{result}</strong>'f'<i>{result}</i>'
    return obertka

@decorator12
def decorate_text1_v2(text):
    return text
def created_by_me(func):
    author_name = "Калиев Мади"
    func.__doc__ = f"Автор: {author_name}\n\n{func.__doc__}" if func.__doc__ else f"Автор: {author_name}"
    return func

@created_by_me
def a():
    pass

text = input("Введите текст: ")
decorated_text = decorate_text(text)
decorr = decorate_text1_v1(text)
decrrr = decorate_text1_v2(text)
print(decorated_text)
print(decorr)
print(decrrr)
print(a.__doc__)
