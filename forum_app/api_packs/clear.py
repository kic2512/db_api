__author__ = 'kic'
from forum_app.api_packs.db_queries.queries import exec_sql


def truncate_all():

    code = 0
    tables = ['Post', 'Thread', 'Forum', 'User', 'Subscribe', 'Followers']
    tbl_list = []
    for x in tables:
        sql = 'truncate %s ;' % x
        tbl_list.append(sql)

    exec_sql(tbl_list, multi=True)
    resp_dict = {'code': code, 'response': 'Ok'}

    return resp_dict
