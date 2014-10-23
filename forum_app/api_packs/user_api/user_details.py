__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, open_sql_all, build_sql_insert_query, \
    build_sql_select_all_query
from forum_app.api_packs.make_response.make_response import make_response


def get_details_user(data, by_id=False):

    code = 0
    keys = []
    values = []

    email = data['user'][0]
    col_name = 'email'
    col_val = email

    if by_id:
        col_name = 'id'
        col_val = data['user_id'][0]

    sql_scheme = {
        'columns_names': [col_name],
        'columns_values': [col_val],
        'table': 'User'
    }

    sql_check = build_sql_select_all_query(sql_scheme)
    res = open_sql(sql_check)  # check if exists

    if not res:
        code = 1
    else:
        sql_scheme_get_followers = {
            'columns_names': ['followee', 'isDeleted'],
            'columns_values': [res['id'], 0],
            'table': 'Followers'
        }

        sql_scheme_get_following = {
            'columns_names': ['follower', 'isDeleted'],
            'columns_values': [res['id'], 0],
            'table': 'Followers'
        }

        sql_get_followers_usr1 = build_sql_select_all_query(sql_scheme_get_followers, what=' id ')
        sql_get_following_usr1 = build_sql_select_all_query(sql_scheme_get_following, what=' id ')

        followers_id = open_sql_all(sql_get_followers_usr1)
        following_id = open_sql_all(sql_get_following_usr1)

        sql_scheme_get_subscriptions = {
            'columns_names': ['user'],
            'columns_values': [res['id']],
            'table': 'Subscribe'
        }
        sql_get_subscriptions = build_sql_select_all_query(sql_scheme_get_subscriptions, what=' thread ')

        subscriptions = open_sql_all(sql_get_subscriptions)

        followers_list = []
        following_list = []
        subscriptions_list = []

        if followers_id:
            for x in followers_id:
                user_data = {'user_id': [x['id'], ], 'user': [None, ]}

                user_resp = get_details_user(user_data, by_id=True)['response']
                followers_list.append(user_resp['email'])

        if following_id:
            for x in following_id:
                user_data = {'user_id': [x['id'], ], 'user': [None, ]}
                user_resp = get_details_user(user_data, by_id=True)['response']
                following_list.append(user_resp['email'])

        if subscriptions:
            for x in subscriptions:
                subscriptions_list.append(x['thread'])

        keys = ['about', 'email', 'followers', 'following', 'id', 'isAnonymous', 'name', 'subscriptions', 'username']
        values = [res['about'], res['email'], followers_list, following_list, int(res['id']), bool(res['isAnonymous']), res['name'],
                  subscriptions_list, res['username']]

    resp_dict = make_response(keys, values, code)

    return resp_dict
