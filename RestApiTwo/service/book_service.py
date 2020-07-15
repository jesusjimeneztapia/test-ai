import requests

from service import OPEN_LIBRA ,OPEN_LIBRA_BOOK_ID

def get_book(id: int):
    url_book = OPEN_LIBRA + (OPEN_LIBRA_BOOK_ID % (id))
    books = requests.get(url_book).json()
    return books