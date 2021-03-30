#exceptions.py

from flask import jsonify

class AppError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

class BadUsageError(AppError):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

class NoRequestBodyError(AppError):
    status_code = 400
    message = "No body present in request."

    def __init__(self, payload=None):
        Exception.__init__(self)
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv
    
class MissingAttributeError(AppError):
    status_code = 400

    def __init__(self, attribute, payload=None):
        Exception.__init__(self)
        self.payload = payload
        self.message = f"Missing attribute: '{attribute}'"

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


class UnauthorizedError(AppError):
    status_code = 401

    def __init__(self, message, payload=None):
        Exception.__init__(self)
        self.message = message
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

class NonExistingResourceError(AppError):
    status_code = 400
    message = "Resource does not exist."

    def __init__(self, key=None, payload=None):
        Exception.__init__(self)
        self.message = f"Resource '{key}' does not exist." if key else "Resource does not exist."
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

class InternalServerError(Exception):
    status_code = 500
    message = "There was an internal server error"

    def __init__(self, payload=None):
        Exception.__init__(self)
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

class UniqueTokenError(AppError):
    status_code = 500

    def __init__(self, resource, payload=None):
        Exception.__init__(self)
        self.payload = payload
        self.message = f"There was a problem creating resource: {resource}. Please try again."

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

class StripeError(AppError):
    # Basic AppError functionality, however, it returns a 'type' field
    # which will help the frontend application know that the error occured
    # was handled by the API (type: 'api')

    status_code = 400 

    def __init__(self, message):
        Exception.__init__(self)
        self.payload = {'type': 'api'}
        self.message = message


    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


def handle_error(error):
    print(error.payload)
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
