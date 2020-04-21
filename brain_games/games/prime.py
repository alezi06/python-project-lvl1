import random
import math

MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num < 2:
        return False
    counter = 3
    stop_num = math.sqrt(num)
    while counter <= stop_num:
        if num % counter == 0:
            return False
        counter += 2
    return True


def round():
    num = random.randint(1, 1000)
    question = str(num)
    answer = 'yes' if is_prime(num) else 'no'
    return (question, answer)
