import random

MESSAGE = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10


def round():
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    hidden_element_position = random.randint(0, PROGRESSION_LENGTH - 1)

    progression = [str(start + step * i) for i in range(PROGRESSION_LENGTH)]
    answer = progression[hidden_element_position]
    progression[hidden_element_position] = '..'
    question = ' '.join(progression)
    return (question, answer)
