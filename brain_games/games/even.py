import random
from brain_games.engine import run_game

MESSAGE = 'Answer "yes" if number even otherwise answer "no".'


def _is_even(num):
    return num % 2 == 0


def _get_question_answer():
    num = random.randint(1, 100)
    answer = 'yes' if _is_even(num) else 'no'
    question = str(num)
    return (question, answer)


def brain_even():
    return run_game(MESSAGE, _get_question_answer)
