import random

MESSAGE = 'Answer "yes" if number even otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def round():
    num = random.randint(1, 100)
    answer = 'yes' if is_even(num) else 'no'
    question = str(num)
    return (question, answer)
