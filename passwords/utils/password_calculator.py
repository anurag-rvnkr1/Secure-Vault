import math

def estimate_cracking_time(password_length, use_numbers, use_symbols, use_special_chars):
    """
    Estimate the cracking time for a given password based on its length and complexity.
    
    :param password_length: Length of the password.
    :param use_numbers: Boolean indicating whether numbers are used.
    :param use_symbols: Boolean indicating whether symbols are used.
    :param use_special_chars: Boolean indicating whether special characters are used.
    
    :return: Estimated cracking time as a string (e.g., '5 hours', '3 days', etc.)
    """
    # Define the character set sizes
    char_set_size = 26  # Lowercase characters

    # Add uppercase letters (A-Z)
    char_set_size += 26

    # Add digits (0-9)
    if use_numbers:
        char_set_size += 10

    # Add special characters (e.g., ~!@#$%^&*)
    if use_symbols:
        char_set_size += 32  # Approximation for common special characters

    # Add more special characters if the 'use_special_chars' is True
    if use_special_chars:
        char_set_size += 10  # Approximate count for other special characters

    # Calculate the cracking time (in seconds) assuming a brute-force attack
    cracking_time_in_seconds = math.pow(char_set_size, password_length) / 1000000000000  # In trillions of attempts per second
    
    # Convert the time to a readable format
    if cracking_time_in_seconds < 60:
        return f"{round(cracking_time_in_seconds)} seconds"
    elif cracking_time_in_seconds < 3600:
        return f"{round(cracking_time_in_seconds / 60)} minutes"
    elif cracking_time_in_seconds < 86400:
        return f"{round(cracking_time_in_seconds / 3600)} hours"
    else:
        return f"{round(cracking_time_in_seconds / 86400)} days"
