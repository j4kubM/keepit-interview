from urllib import request
from html.parser import HTMLParser

class MyParser(HTMLParser):
    def __init__(self):
        super(MyParser, self).__init__()
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

def main():
    url = input("Please provide the url:\n")
    print(url)
    try: 
        response = request.urlopen(url)
        html_response = response.read().decode('utf-8')
        parser = MyParser()
        parser.feed(html_response)
        last_item = parser.last_item
        if last_item:
            print(f"Last item from the unordered list: {last_item}")
        else:
            print("No unordered list found")
    except Exception as e:
        print(f"Error fetching content from {url}:{e}")     
if __name__ == "__main__":
    main()