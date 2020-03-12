import random
from brain_games.engine import run_game

MESSAGE = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10


def _get_progression(start, step, length):
    return [str(start + step * i) for i in range(length)]


def _get_question_answer():
    start_progression = random.randint(1, 10)
    step_progression = random.randint(1, 10)
    hidden_element_position = random.randint(0, PROGRESSION_LENGTH - 1)

    progression = _get_progression(
        start_progression,
        step_progression,
        PROGRESSION_LENGTH
    )
    answer = progression[hidden_element_position]
    question = ' '.join(progression).replace(answer, '..')
    return (question, answer)


def brain_progression():
    return run_game(MESSAGE, _get_question_answer)
