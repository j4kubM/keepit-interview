from urllib import request
from html_extractor import HtmlExtractor

def main():
    url = input("Please provide the url:\n")
    try: 
        response = request.urlopen(url)
        html_content = response.read().decode('utf-8')
        extractor = HtmlExtractor()
        print(extractor.extractUnorderedListLastItem(html_content))
    except Exception as e:
        print(f"Error fetching content from {url}:{e}")     
if __name__ == "__main__":
    main()