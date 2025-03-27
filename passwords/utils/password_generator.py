# utils/password_generator.py

import random
import string

def generate_password(length=12, include_numbers=True, include_symbols=True):
    """
    Generates a strong random password based on user-defined criteria.
    :param length: Length of the password (default is 12)
    :param include_numbers: Whether to include numbers (default is True)
    :param include_symbols: Whether to include symbols (default is True)
    :return: Generated password
    """
    # Start with basic alphabet characters
    characters = string.ascii_letters

    # Add numbers if requested
    if include_numbers:
        characters += string.digits
    
    # Add symbols if requested
    if include_symbols:
        characters += string.punctuation

    # Generate a password by randomly choosing characters
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password
