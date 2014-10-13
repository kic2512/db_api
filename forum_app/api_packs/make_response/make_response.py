__author__ = 'kic'


def make_response(keys, values, code=0):
    a = dict(zip(keys, values))

    response = {'code': code, 'response': a}
    return response
