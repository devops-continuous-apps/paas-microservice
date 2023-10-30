import unittest
from src.errors.errors import InvalidToken, InvalidParams, EmailAlreadyExists


class TestApiErrors(unittest.TestCase):
    def test_invalid_params(self):
        error = InvalidParams()
        self.assertEqual(error.description, "Invalid parameters")
        self.assertEqual(error.code, 400)

    def test_invalid_token(self):
        error = InvalidToken()
        self.assertEqual(error.description, "Unauthorized")
        self.assertEqual(error.code, 401)

    def test_email_already_exists(self):
        error = EmailAlreadyExists()
        self.assertEqual(error.description, "Email already exists in the blacklist")
        self.assertEqual(error.code, 412)


if __name__ == '__main__':
    unittest.main()
