__author__ = 'kic'
from forum_app.settings import ERRORS_MESSAGES
from datetime import datetime


def make_response(keys=[], values=[], code=0, sql='no'):
    if code != 0:
        response = {'code': code, 'response': ERRORS_MESSAGES[code]}
        return response

    a = dict(zip(keys, values))

    response = {'code': code, 'response': a}

    return response
