from flask import Flask, jsonify
from app.core.notfoundexception import NotFoundException
def error_handlers(app:Flask):
      @app.errorhandler(NotFoundException)
      def not_found_exception_handler(e:NotFoundException): 
            response = {
                  "message" :e.message
            }
            return jsonify(response), e.code
