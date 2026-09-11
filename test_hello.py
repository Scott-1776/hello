import unittest
from unittest.mock import patch

import hello


class HelloTests(unittest.TestCase):
    def test_greet_uses_default_punctuation(self):
        self.assertEqual(hello.greet("Ada"), "Hello, Ada!")

    def test_greet_trims_name_and_accepts_custom_punctuation(self):
        self.assertEqual(hello.greet(" Ada ", "?"), "Hello, Ada?")

    def test_main_uses_default_name(self):
        with patch("builtins.print") as print_mock:
            hello.main([])

        print_mock.assert_called_once_with("Hello, world!")

    def test_main_accepts_name_and_punctuation(self):
        with patch("builtins.print") as print_mock:
            hello.main(["Ada", "--punctuation", "."])

        print_mock.assert_called_once_with("Hello, Ada.")

    def test_greet_rejects_blank_name(self):
        with self.assertRaises(ValueError):
            hello.greet("   ")

    def test_greet_rejects_invalid_punctuation(self):
        with self.assertRaises(ValueError):
            hello.greet("Ada", ",")

    def test_version(self):
        with patch("sys.stdout") as stdout_mock:
            with self.assertRaises(SystemExit) as exit_info:
                hello.main(["--version"])

        self.assertEqual(exit_info.exception.code, 0)
        stdout_mock.write.assert_called_once_with("0.1.0\n")


if __name__ == "__main__":
    unittest.main()