__author__ = 'kic'
from forum_app.api_packs.db_queries.queries import exec_sql


def truncate_all():

    code = 0
    tables = ['Post', 'Thread', 'Forum', 'User']
    for x in tables:
        sql = 'truncate %s' % x
        exec_sql(sql)

    resp_dict = {'code': code, 'response': 'Ok'}

    return resp_dict
