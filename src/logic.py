import wikipedia
from textblob import TextBlob


def wiki(name="Artificial Intelligence", length=1):
    """Fetches data  from Wikipedia"""
    try:
        my_wiki = wikipedia.summary(name, length)
    except wikipedia.exceptions.PageError:
        my_wiki = f"No page found for '{name}'"
    except wikipedia.exceptions.DisambiguationError as e:
        my_wiki = f"Disambiguation error: {e.options}"
    return my_wiki


def wiki_search(name):
    """Fetches search results from Wikipedia"""

    my_wiki = wikipedia.search(name)
    return my_wiki


def phrase(name):
    """Returns phrase from Wikipedia summary"""

    page = wiki(name)
    phrases = TextBlob(page).noun_phrases
    return phrases
