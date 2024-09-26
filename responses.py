from random import choice, randint
def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfullysilent...'
    elif 'hello' in lowered:
        return 'Hello there'
    elif 'hello there' in lowered:
        return 'General Kenobi'
    elif 'hogy vagy' in lowered:
        return 'Köszi jól'
    elif 'bye' in lowered:
        return 'See you'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1,6)}'
    else:
        return choice(['MILYEN CSODÁS EZ A NAP',
                      'Bober',
                      'Hol a fa főnök?'])