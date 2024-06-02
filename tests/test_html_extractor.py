import unittest
from src.html_extractor import HtmlExtractor

class TestHtmlExtractor(unittest.TestCase):
    def test_extractUnorderedListLastItem(self):
        # Create an instance of HtmlExtractor
        extractor = HtmlExtractor()

        # Test case 1: When there is an unordered list
        with open("data/list.html", "r") as f:
            html_content = f.read()
        expected_result = "Last item from the unordered list: Item 3"
        self.assertEqual(extractor.extractUnorderedListLastItem(html_content), expected_result)

        # Test case 2: When there is no unordered list
        with open("data/no_list.html", "r") as f:
            html_content = f.read()
        expected_result = "No unordered list found"
        self.assertEqual(extractor.extractUnorderedListLastItem(html_content), expected_result)