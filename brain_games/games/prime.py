import random
from brain_games.engine import run_game

MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def _is_prime(num):
    if num < 2:
        return False
    counter = 2
    while counter <= num // 2:
        if num % counter == 0:
            return False
        counter += 1
    return True


def _get_question_answer():
    num = random.randint(1, 1000)
    question = str(num)
    answer = 'yes' if _is_prime(num) else 'no'
    return (question, answer)


def brain_prime():
    return run_game(MESSAGE, _get_question_answer)
