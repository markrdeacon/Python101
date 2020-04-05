"""Retrieve and print strings from a url

Usage:
    python words.py <url>
"""
import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a url
    Args:
        url: The URL of the UTF8 document
    Returns:
        A list of strings containing the words from the document
    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(items):
    """Print items, one per line
    Args: 
        An iterative series of items to print
    """
    for item in items:
        print(item)


def main(url):
    """Print each word of a document at a url
    Args:
        url: the url of the UTF8 document
    """
    words = fetch_words(url)
    print_items(words)


# execute if not imported into module
if __name__ == "__main__":
    url = sys.argv[1]
    main(url)
