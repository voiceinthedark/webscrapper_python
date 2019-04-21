"""Web scrapping module"""
import requests
from bs4 import BeautifulSoup


class WebScrapper:
    """Web scrapper class.
    Contains the following methods:
    __init__: the class constructor
    _captureurl: private method called from the constructor that capture
        the url argument passed to the constructor and checks for ok response
    checkstatus: method to check the url response code
    captureselector: main class method that capture a css selector by type
    savereport: this method will save the data scrapped into a file on HD
    print2screen: Method that prints the data output to the console"""

    def __init__(self, link):
        """Constructor, accepts a link to url to scrap.

        Arguments:
        link: the url link that need to be scrapped
        response: the response of the url link
        links: initiailize empty list to collect the scrapped data"""

        self.link = link
        self.response = self._captureurl(link)
        self.links = []

    def __captureurl(self, link):
        """Capture the url with the requests module and check for connection
        errors"""

        self.res = requests.get(self.link,)
        self.res.raise_for_status()
        return self.res

    def checkstatus(self):
        """Check the response connection status"""

        print(self.response)

    def captureselector(self, selector='a'):
        """Method captureselector will capture all elements by selector type.

        Arguments:
        selector: default to <a>, the other case would be <img>"""

        soup = BeautifulSoup(self.response.text, 'html.parser')
        # print(soup)
        list_links = soup.find_all(selector)
        for l in list_links:
            self.links.append(l)
        return self.links

    def savereport(self, file='report.txt', type='href'):
        """Method savereport will save the captured contents into a file
        on disk.

        Arguments:
        file(optional): the name of the file, default: report.txt"""

        with open(file, 'w') as f:
            # fill title
            title = ' Scrapping report for {} '.format(self.link)
            f.write(title.center(79, ' ') + '\n'*3)
            for l in self.links:
                li = str(l.get(type))
                if not li.startswith('#') and not li == None:
                    if not li.startswith('http'):
                        f.write(self.link + '/' + li + '\n')
                    else:
                        f.write(li + '\n')

    def print2screen(self, type='href'):
        """Method print2screen will output the data to screen.
        Optional Arguments:
        type: can be 'href' or 'src' depending on whether the user provided
                -l or -i for links and images respectively"""

        for l in self.links:
            link = str(l.get(type))
            if not link.startswith('http'):
                link = self.link + '/' + link
            print(link)

if __name__ == '__main__':
    ws = WebScrapper("http://inventwithpython.com")
    for i in ws.captureselector():
        print(i)
    ws.savereport()
