import wikipedia


def wiki(name="Artificial Intelligence", length=1):
    """Fetches data  from Wikipedia"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki
