from flask import jsonify, request
from controller import API_BOOK
from service import book_service
from http_code import *
from exception import ExceptionResponse

def get_instance(app):
    @app.route(API_BOOK, methods=['GET'])
    def index():
       return 'Welcome api books.'

    @app.route(API_BOOK + '/<int:id>', methods=['GET'])
    def get_book(id):
        status = HTTP_OK
        books = book_service.get_book(id)
        if (books.__len__() == 0):
            message = 'El libro con id %d no fue encontrado.' % (id)
            response = ExceptionResponse(message, HTTP_NOT_FOUND)
            status = response.status
        else:
            response = books[0]
        return jsonify(response), status