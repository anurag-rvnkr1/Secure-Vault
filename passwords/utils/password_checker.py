# utils/password_checker.py

import re

def check_password_strength(password):
    """
    Checks the strength of the password and provides suggestions.
    :param password: The password to check
    :return: Tuple containing the strength of the password and a list of suggestions
    """
    strength = "Weak"
    suggestions = []

    # Check password length
    if len(password) < 8:
        suggestions.append("Password should be at least 8 characters.")
    
    # Check if password contains at least one digit
    if not re.search(r"\d", password):
        suggestions.append("Password should contain at least one number.")
    
    # Check if password contains at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        suggestions.append("Password should contain at least one uppercase letter.")
    
    # Check if password contains at least one lowercase letter
    if not re.search(r"[a-z]", password):
        suggestions.append("Password should contain at least one lowercase letter.")
    
    # Check if password contains at least one special character
    if not re.search(r"[@$!%*?&]", password):
        suggestions.append("Password should contain at least one special character.")

    # Password strength classification
    if len(password) >= 12 and re.search(r"\d", password) and re.search(r"[A-Z]", password) and re.search(r"[a-z]", password) and re.search(r"[@$!%*?&]", password):
        strength = "Strong"
    elif len(password) >= 8:
        strength = "Medium"

    return strength, suggestions
