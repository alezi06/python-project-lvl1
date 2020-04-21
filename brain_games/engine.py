import brain_games.cli as cli

ROUNDS_COUNT = 3


def run(game):
    cli.welcome_game(game.MESSAGE)
    user_name = cli.get_user_name()
    cli.welcome_user(user_name)

    counter = 0
    while counter < ROUNDS_COUNT:
        question, answer = game.round()

        cli.print_question(question)
        player_answer = cli.get_player_answer()

        if answer != player_answer:
            cli.incorrect_answer(answer, player_answer, user_name)
            return

        cli.correct_answer()
        counter += 1

    cli.print_congratulation(user_name)
