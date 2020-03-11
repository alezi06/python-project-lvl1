import random
from brain_games.engine import run_game

MESSAGE = 'Find the greatest common divisor of given numbers.'


def _get_common_divisor(first, second):
    min_num = min(first, second)
    max_num = max(first, second)

    def inner(max, min):
        mod = max % min
        if mod == 0:
            return min
        return inner(min, mod)

    return inner(max_num, min_num)


def _get_question_answer():
    first = random.randint(1, 100)
    second = random.randint(1, 100)

    question = f"{first} {second}"
    answer = str(_get_common_divisor(first, second))
    return (question, answer)


def brain_gcd():
    return run_game(MESSAGE, _get_question_answer)
