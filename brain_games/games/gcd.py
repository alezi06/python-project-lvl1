import random

MESSAGE = 'Find the greatest common divisor of given numbers.'


def gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


def round():
    first = random.randint(1, 100)
    second = random.randint(1, 100)

    question = f"{first} {second}"
    answer = str(gcd(first, second))
    return (question, answer)
