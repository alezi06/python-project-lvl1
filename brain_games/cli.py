import prompt


def welcome_game(message):
    print('Welcome to the Brain Games!')
    print(message)
    print()


def get_user_name():
    user_name = prompt.string('May I have your name? ')
    return user_name


def welcome_user(user_name):
    print(f"Hello, {user_name}!")
    print()


def print_question(question):
    print(f"Question: {question}")


def get_player_answer():
    answer = prompt.string('Your answer: ')
    return answer


def incorrect_answer(answer, player_answer, user_name):
    print(
        f"'{player_answer}' is wrong answer ;(. Correct answer was '{answer}'."
    )
    print(f"Let's try again, {user_name}!")


def correct_answer():
    print('Correct!')


def print_congratulation(user_name):
    print(f"Congratulations, {user_name}!")
