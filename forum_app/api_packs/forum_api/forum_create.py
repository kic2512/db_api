__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, build_sql_insert_query, \
    build_sql_select_all_query
from forum_app.api_packs.make_response.make_response import make_response
from forum_app.api_packs.user_api.user_details import get_details_user


def create_forum(data):
    code = 0
    name = data['name'].encode("utf-8")
    shn = data['short_name'].encode("utf-8")
    usr = data['user'].encode("utf-8")

    usr_details = get_details_user({'user': [usr, ]})
    usr_id = usr_details['response']['id']

    #sql_check = "select id,name,short_name,user from Forum where name = '%s' and short_name = '%s' " % (name, shn)
    sql_scheme = {
        'columns_names': ['name'],
        'columns_values': [name],
        'table': 'Forum'
    }

    sql_check = build_sql_select_all_query(sql_scheme)

    res = open_sql(sql_check)  # check if exists
    if not res:
        sql_scheme = {
            'columns_names': ['name', 'short_name', 'user'],
            'columns_values': [name, shn, usr_id],
            'table': 'Forum'
        }

        sql = build_sql_insert_query(sql_scheme)
        exec_message = exec_sql(sql)
        if exec_message == 0:
            res = open_sql(sql_check)
        else:
            code = 4

    keys = ['id', 'name', 'short_name', 'user']
    values = [int(res['id']), res['name'], res['short_name'], usr]
    resp_dict = make_response(keys, values, code)

    return flask.jsonify(resp_dict)

