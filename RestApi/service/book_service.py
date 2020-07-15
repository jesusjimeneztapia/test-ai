import requests

from service import REST_API_TWO, REST_API_BOOK_ID

def get_book(id: int):
    url_book = REST_API_TWO + (REST_API_BOOK_ID % (id))
    book = requests.get(url_book)
    return book
