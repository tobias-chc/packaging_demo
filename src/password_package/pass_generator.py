import random
import math
import string


def get_password_length_input(min_length = 6, max_length = 15):
    """
    Get the password length from the user , it needs to be a integer between
    min_length and max_length, this length includes all the characters
    (numbers, letters, special characters).

    Args:
        min_length (int): Minimum length of the password, 6 by default.
        max_length (int): Maximum length of the password, 15 by default.

    Returns:
        int: The length of the password.
    """

    try:
        # Convert it into integer
        pass_length = int(input("Enter the length of your password: ").rstrip())
    except ValueError as e:
        print("Password lenght must be an integer")
    else:
        # Skipped if there is an exception.
        length_cond = pass_length in range(min_length, max_length + 1)
        if length_cond:
            return pass_length
        else:
            print('Password lenght is not valid.')



def generate_component(length, characters, is_alpha = False):

    """
    Generate a random password of a given length and a set of chracters.

    Args:
        length (int): Length of the password.
        characters (int): Set of characters available.
        is_alpha (boolean): When chracters are letters activate upper
                            case option, False by default.

    Returns:
        str: Password generated.
    """

    password = []

    for i in range(length):
        index = random.randint(0, len(characters) - 1)
        character = characters[index]
        if is_alpha:
            case = random.randint(0, 1)
            if case == 1:
                character = character.upper()
        password.append(character)

    return password


def create_password():
    """
    Generate a password of a given length defined by the user, the password
    contains digits, letters and special characters with the following
    proportion (50%, 30%, 20%).

    Args:

    Returns:
        str: Password generated.
    """

    pass_length = get_password_length_input()

    if pass_length is not None:
        # length of password by 50-30-20 formula
        alpha_lenght = pass_length//2
        digit_lenght = math.ceil(pass_length*30/100)
        special_length = pass_length - (alpha_lenght + digit_lenght)

        alpha = string.ascii_lowercase
        digit = string.digits
        special_char = string.punctuation



        # alpha component password
        alpha_component =generate_component(alpha_lenght, alpha, True)
        # digit component password
        digit_component = generate_component(digit_lenght, digit)
        # special character componet password
        special_char_component = generate_component(special_length, special_char)

        password = alpha_component + digit_component + special_char_component
        # suffle the generated password list
        random.shuffle(password)

        # convert List To string
        gen_password = ''.join(password)

        return gen_password

    else:
        pass
