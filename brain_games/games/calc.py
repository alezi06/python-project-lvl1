import operator
import random

MESSAGE = 'What is the result of the expression?'
OPERATIONS = (
    ('+', operator.add),
    ('-', operator.sub),
    ('*', operator.mul),
)


def round():
    first = random.randint(1, 100)
    second = random.randint(1, 100)
    symbol, function = random.choice(OPERATIONS)

    question = f"{first} {symbol} {second}"
    answer = str(function(first, second))
    return (question, answer)
