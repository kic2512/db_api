__author__ = 'kic'
from forum_app.settings import ERRORS_MESSAGES
from datetime import datetime


def make_response(keys=[], values=[], code=0, sql='no'):
    if code != 0:

        f = open('/home/kic/flask_proj/forum_app/api_packs/make_response/api.log', 'a')
        f.write(str(datetime.now()))
        f.write(' : ')
        f.write(sql)
        f.write('\n')
        f.close()

        response = {'code': code, 'response': ERRORS_MESSAGES[code]}
        return response

    a = dict(zip(keys, values))

    response = {'code': code, 'response': a}

    return response
