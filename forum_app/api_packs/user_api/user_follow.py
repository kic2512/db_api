__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, open_sql_all, build_sql_insert_query, \
    build_sql_select_all_query
from forum_app.api_packs.make_response.make_response import make_response
from forum_app.api_packs.user_api.user_details import get_details_user


def follow_user(data):
    code = 0

    keys = ['id', 'username', 'about', 'name', 'email', 'isAnonymous', 'followers', 'following', 'subscriptions']
    values = [1, 'noname', 'qwe', 'lal', 'lal@trall.com', 0, 'a', 'b', 'c']

    if not data:
        resp_dict = make_response(keys, values, code=0)
        return flask.jsonify(resp_dict)

    email_1 = data['follower']
    email_2 = data['followee']

    sql_scheme_usr1 = {
        'columns_names': ['email'],
        'columns_values': [email_1],
        'table': 'User'
    }

    sql_scheme_usr2 = {
        'columns_names': ['email'],
        'columns_values': [email_2],
        'table': 'User'
    }

    sql_scheme_follow = {
        'columns_names': ['follower', 'followee'],
        'columns_values': [email_1, email_2],
        'table': 'Followers'
    }

    #!sql_check_usr1 = build_sql_select_all_query(sql_scheme_usr1, what=' id ', limit=1)
    #!sql_check_usr2 = build_sql_select_all_query(sql_scheme_usr2, what=' id ', limit=1)
    sql_check_follow = build_sql_select_all_query(sql_scheme_follow)

    #!res_usr1 = open_sql(sql_check_usr1)  # check if exists
    #!res_usr2 = open_sql(sql_check_usr2)
    res_usr1 = True
    res_usr2 = True

    res_follow = open_sql(sql_check_follow)

    if res_usr1 and res_usr2 and not res_follow:

        sql = build_sql_insert_query(sql_scheme_follow)
        exec_message = exec_sql(sql)

        if exec_message != 0:
            #code = 4
            a = 0

        usr_details = get_details_user({'user': [email_1, ]})

        usr_details = usr_details['response']

        if 'id' in usr_details:
            values = [int(usr_details['id']), usr_details['username'], usr_details['about'], usr_details['name'],
                      usr_details['email'], bool(usr_details['isAnonymous']), usr_details['followers'],
                      usr_details['following'], usr_details['subscriptions']]

    resp_dict = make_response(keys, values, code)
    return flask.jsonify(resp_dict)
