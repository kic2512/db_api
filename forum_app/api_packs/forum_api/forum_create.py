__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, build_sql_query
from forum_app.api_packs.make_response.make_response import make_response


def create_forum(data):
    name = data['name'].encode("utf-8")
    shn = data['short_name'].encode("utf-8")
    usr = data['user'].encode("utf-8")

    sql_check = "select id,name,short_name,user from Forum where name = '%s' and short_name = '%s' " % (name, shn)
    res = open_sql(sql_check)  # check if exists
    if not res:
        sql_scheme = {
            'columns_names': ['name', 'short_name', 'user'],
            'columns_values': [str(name), str(shn), str(usr)],
            'table': 'Forum',
            'type': 'insert'}

        sql = build_sql_query(sql_scheme)
        res = exec_sql(sql)
        if res == 0:
            res = open_sql(sql_check)
        else:
            TODO = None

    keys = ['id', 'name', 'short_name', 'user']
    values = [int(res['id']), res['name'], res['short_name'], res['user']]
    resp_dict = make_response(keys=keys, values=values)

    return flask.jsonify(resp_dict)

