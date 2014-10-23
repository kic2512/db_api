__author__ = 'kic'
import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, build_sql_insert_query, \
    build_sql_select_all_query
from forum_app.api_packs.make_response.make_response import make_response
from forum_app.api_packs.user_api.user_details import get_details_user


def get_details_forum(data):
    code = 0
    keys = []
    values = []

    forum_sh_name = data.get('forum', None)[0]
    #related = data['related'][0]
    related = data.get('related', None)

    sql_scheme = {
        'columns_names': ['short_name'],
        'columns_values': [forum_sh_name],
        'table': 'Forum'
    }

    sql_check = build_sql_select_all_query(sql_scheme)

    res = open_sql(sql_check)  # check if exists

    if not res:
        code = 2
    else:

        sql = 'select * from User where id = %s' % res['user']
        usr = open_sql(sql)
        res['user'] = usr['email']

        if related:
            user_data = {'user': [usr['email'], ]}
            user_resp = get_details_user(user_data)
            res['user'] = user_resp['response']

        keys = ['id', 'name', 'short_name', 'user']
        values = [res['id'], res['name'], res['short_name'], res['user']]

    resp_dict = make_response(keys, values, code)

    return resp_dict

