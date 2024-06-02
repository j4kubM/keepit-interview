from src.parsers import UnorderedListParser


class HtmlExtractor():
    """Extract the desired information from the HTML document"""
    def extractUnorderedListLastItem(self, html_content) -> str:
        """
            Return the last element of the unordered list from the html content, or empty string when there is no list.
        """
        parser = UnorderedListParser()
        parser.feed(html_content)
        last_item = parser.last_item
        if last_item:
            return f"Last item from the unordered list: {last_item}"
        else:
            return "No unordered list found"