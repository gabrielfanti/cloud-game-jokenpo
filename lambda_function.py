import random


def lambda_handler(event, context):
    choices = ['pedra', 'papel', 'tesoura']
    user_choice = event['user_choice']
    machine_choice = random.choice(choices)

    result = determine_winner(user_choice, machine_choice)

    return {
        'user_choice': user_choice,
        'machine_choice': machine_choice,
        'result': result
    }


def determine_winner(user_choice, machine_choice):
    if user_choice == machine_choice:
        return 'Empate'
    elif (
            (user_choice == 'pedra' and machine_choice == 'tesoura') or
            (user_choice == 'papel' and machine_choice == 'pedra') or
            (user_choice == 'tesoura' and machine_choice == 'papel')
    ):
        return 'Você venceu!'
    else:
        return 'Você perdeu!'
