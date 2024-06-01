from urllib import request
from parsers import UnorderedListParser

def main():
    url = input("Please provide the url:\n")
    print(url)
    try: 
        response = request.urlopen(url)
        html_response = response.read().decode('utf-8')
        parser = UnorderedListParser()
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