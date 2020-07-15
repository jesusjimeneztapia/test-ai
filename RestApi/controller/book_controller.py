from flask import jsonify

from controller import API_BOOK
from service import book_service

def get_instance(app):
    @app.route(API_BOOK + '/<int:id>', methods=['GET'])
    def get_book(id: int):
        book = book_service.get_book(id)
        return jsonify(book.json()), book.status_code
