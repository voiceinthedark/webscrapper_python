### Python command-line Web scrapper

#### Description
This is a simple web scrapper, that uses the [requests library](https://2.python-requests.org//en/master/) as well as the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) library to scrape web pages for links and images.

#### Usage
```
wsm.py [-h] [-l] [-i] [-s (filename)] [-p] link_to_website  

[-l] or --link flag (default) will scrap links with href
[-i] or --image flag will scrap images with src
[-s] or --save (filename) will accept a filename to save
     a report with the links captured. if no -s was set
     the script will save a report with 'report.txt' in
     the same directory as the script
[-p] or --print if the this flag is set, the script will
     output its data to the console
```
