from html.parser import HTMLParser
import urllib.request

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print('Encountered comment:', data)
        pos = self.getpos()
        print('\tat line:', pos[0], 'position', pos[1])

parser = MyHTMLParser()
web_url = urllib.request.urlopen('http://www.kirkkittell.com')
contents = web_url.read()
parser.feed(str(contents))