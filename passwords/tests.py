from django.test import TestCase
from .utils.password_checker import check_password_strength
from .utils.password_generator import generate_password

class PasswordUtilsTests(TestCase):

    def test_password_strength_checker(self):
        strength, suggestions = check_password_strength("Test@123")
        self.assertEqual(strength, "Very Strong")
        self.assertEqual(len(suggestions), 0)

    def test_password_generator(self):
        password = generate_password(length=12, use_numbers=True, use_symbols=True, use_special_chars=True)
        self.assertEqual(len(password), 12)
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(char in "!@#$%^&*()" for char in password))


        
