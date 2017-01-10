#!/usr/bin/env python3

"""
Working with BeautifulSoup 4.
"""

from urllib.parse import urljoin

from bs4 import BeautifulSoup


def to_soup(html_source, parser='html.parser'):
    """Convert HTML source (text) to soup object.

    parser can be:
    * html.parser (Python's html.parser)
    * lxml (lxml's HTML parser)  -- FASTEST
    * xml (lxml's XML parser)
    * html5lib
    """
    return BeautifulSoup(html_source, parser)


def prettify(soup):
    """
    Prettify HTML source. The HTML source is in a soup object.
    The return value is a string!
    """
    return soup.prettify()


def get_links(soup, base_url=None):
    """
    Get the links on a webpage. If the URL of the given
    page is provided in base_url, then links are absolute.

    The soup object is NOT modified.
    """
    li = []
    for tag in soup.findAll('a', href=True):
        if base_url:
            link = urljoin(base_url, tag['href'])
        else:
            link = tag['href']

        li.append(link)

    return li


def get_images(soup, base_url=None):
    """
    Get image src's on a webpage. If the URL of the given
    page is provided in base_url, then links are absolute.

    The soup object is NOT modified.
    """
    li = []
    for tag in soup.findAll('img', src=True):
        if base_url:
            link = urljoin(base_url, tag['src'])
        else:
            link = tag['src']

        li.append(link)

    return li


def make_links_absolute(soup, base_url):
    """
    Replace relative links with absolute links.
    This one modifies the soup object.
    """
    assert base_url is not None
    #
    for tag in soup.findAll('a', href=True):
        tag['href'] = urljoin(base_url, tag['href'])

    return soup
