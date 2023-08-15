from html.parser import HTMLParser


class Arma3HTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            if len(attrs) == 2:
                if attrs[1] == ('data-type', 'Link'):
                    name, value = attrs[0]
                    self.urls.append(value)
            '''
            # get any link
            for name, value in attrs:
                if name == 'href':
                    print(name, value)
            '''

    def error(self, message):
        print(message)
        raise RuntimeError


def parse(file):
    ids = []
    parser = Arma3HTMLParser()
    parser.feed(file.read())
    for url in parser.urls:
        ids.append(url.split('id=')[1])
    return ids
