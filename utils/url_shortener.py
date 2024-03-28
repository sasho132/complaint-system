import pyshorteners

shortener = pyshorteners.Shortener()


def shorten_url(url):
    return shortener.tinyurl.short(url)
