import unittest
from app.io.input import input_text_file, input_text_pandas


class TestInputFile(unittest.TestCase):

    def test_file_exists(self):
        file_content = input_text_file("test_file.txt")
        self.assertIsNotNone(file_content)

    def test_file_content(self):
        expected_content = "Test content"
        with open("test_file.txt", "w") as f:
            f.write(expected_content)
        file_content = input_text_file("test_file.txt")
        self.assertEqual(file_content, expected_content)

    def test_empty_file(self):
        with open("empty_file.txt", "w") as f:
            pass  # Create an empty file
        file_content = input_text_file("empty_file.txt")
        self.assertEqual(file_content, "")
