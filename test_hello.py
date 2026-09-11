import unittest
from unittest.mock import patch

import hello


class HelloTests(unittest.TestCase):
    def test_greet_returns_greeting(self):
        self.assertEqual(hello.greet("Ada"), "Hello, Ada!")

    def test_main_accepts_arguments(self):
        with patch("builtins.print") as print_mock:
            hello.main(["Ada"])

        print_mock.assert_called_once_with("Hello, Ada!")

    def test_greet_rejects_blank_name(self):
        with self.assertRaises(ValueError):
            hello.greet("   ")


if __name__ == "__main__":
    unittest.main()