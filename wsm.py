from argparse import ArgumentParser
from ws import WebScrapper

parser = ArgumentParser(description='Web Scrapper')

def setup_parser():
    """Function setup_parser will setup the argument parser with the Arguments
    we will be catching.

    Arguments:
    -l: links, capture every <a> tag in the document
    -i: images, capture every <img> tag in the document
    -p: print, print the output to the console
    -s: save, save a report with the data scrapped to hard disk,
        default: report.txt"""
        
    parser.add_argument('url', type=str, help='The url link to be scrapped')
    parser.add_argument('-l', '--link', action='store_true',
        help='Web scrapper will scrap for links')
    parser.add_argument('-i', '--image', action='store_true',
        help='Web scrapper will scrap for images')
    parser.add_argument('-p', '--print', action= 'store_true',
        help='Web scrapper will output to console')
    parser.add_argument('-s', '--save', nargs='?', type=str,
        default='report.txt', help='An optional file to save a report to' +
        ' will default to "report.txt" if no argument is provided')

setup_parser()
args = parser.parse_args()

# capture the link
scrap = WebScrapper(args.url)
# if -l flag was provided, capture all href links
if args.link:
    scrap.captureselector()
    # if -p flag was set, print to screen
    if args.print:
        scrap.print2screen()
# if -i flag was set, collect img tags
if args.image:
    scrap.captureselector('img')
    if args.print:
        scrap.print2screen('src')
# if -s was set, save file with the scrapped data, will default to 'report.txt'
if args.save:
    if args.image:
        scrap.savereport(args.save, type='src')
    if args.link:
        scrap.savereport(args.save)
