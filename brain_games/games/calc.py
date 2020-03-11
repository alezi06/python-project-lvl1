import operator
import random
from brain_games.engine import run_game

MESSAGE = 'What is the result of the expression?'
OPERATORS = ('+', '-', '*')
OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def _calculate(first, second, operator):
    return OPERATIONS[operator](first, second)


def _get_question_answer():
    first = random.randint(1, 100)
    second = random.randint(1, 100)
    operator = random.choice(OPERATORS)

    question = f"{first} {operator} {second}"
    answer = str(_calculate(first, second, operator))
    return (question, answer)


def brain_calc():
    return run_game(MESSAGE, _get_question_answer)
