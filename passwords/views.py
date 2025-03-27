from django.shortcuts import render, redirect
from .utils.password_checker import check_password_strength
from .utils.password_generator import generate_password  # Fixed import
from .utils.password_calculator import estimate_cracking_time
import string
import random


# Redirect to the password strength checker or generator by default
def homepage(request):
    return render(request, 'homepage.html')


# Password Strength Checker View
def check_password(request):
    result = None
    suggestions = []

    if request.method == 'POST':
        password = request.POST.get('password')
        result, suggestions = check_password_strength(password)

    return render(request, 'check_password.html', {
        'result': result,
        'suggestions': suggestions
    })


# Password Generator View
def generate_password_view(request):
    generated_password = ''

    if request.method == 'POST':
        length = int(request.POST.get('length', 12))  # Default length is 12
        use_numbers = 'use_numbers' in request.POST
        use_symbols = 'use_symbols' in request.POST
        use_special_chars = 'use_special_chars' in request.POST

        # Use the correct function for generating passwords
        generated_password = generate_password(length, use_numbers, use_symbols, use_special_chars)

    return render(request, 'generate_password.html', {
        'password': generated_password
    })


# Password Generation Logic (Utils Function)
def generate_password(length=12, use_numbers=True, use_symbols=True, use_special_chars=False):
    chars = string.ascii_letters  # Uppercase & lowercase letters by default

    if use_numbers:
        chars += string.digits  # Add digits if selected
    if use_symbols:
        chars += string.punctuation  # Add punctuation (symbols) if selected
    if use_special_chars:
        chars += "!@#$%^&*()_+"  # Custom additional special characters

    return ''.join(random.choice(chars) for _ in range(length))
