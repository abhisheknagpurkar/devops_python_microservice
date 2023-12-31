import wikipedia
from textblob import TextBlob


def wiki(name="War Goddess", length=1):
    """This is a wikipedia fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def search_wiki(name):
    """Search Wikipedia by name"""

    results = wikipedia.search(name)
    return results


def phrases(name):
    """Retrieve phrases from Wikipedia page"""

    page = wiki(name)
    blob = TextBlob(page)
    return blob.noun_phrases
