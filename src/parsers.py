from html.parser import HTMLParser

class UnorderedListParser(HTMLParser):
    def __init__(self):
        super(UnorderedListParser, self).__init__()
        self.in_ul = False
        self.last_item = None

    def handle_starttag(self, tag, attrs):
        if tag == 'ul':
            self.in_ul = True

    def handle_endtag(self, tag):
        if tag == 'ul':
            self.in_ul = False

    def handle_data(self, data):
        if self.in_ul and data.strip() !="":
            self.last_item = data.strip()