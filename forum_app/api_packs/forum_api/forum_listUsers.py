__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, open_sql_all, build_sql_insert_query, \
    build_sql_select_all_query
from forum_app.api_packs.make_response.make_response import make_response
from forum_app.api_packs.user_api.user_details import get_details_user


def get_forum_users_list(data):
    code = 0
    posts_list = []
    users_res = []

    forum_sh_name = data.get('forum')[0]

    since = data.get('since_id', [0, ])[0]

    limit = data.get('limit', [1, ])[0]

    is_desc = 0
    order_by = data.get('order', 'desc')
    if 'desc' in order_by:
        is_desc = 1

    sql_scheme = {
        'columns_names': ['short_name'],
        'columns_values': [forum_sh_name],
        'table': 'Forum'
    }
    #sql_check = build_sql_select_all_query(sql_scheme)

    # res = open_sql(sql_check)  # check if exists

    res = True
    if not res:
        code = 2
    else:
        sql_scheme = {
            'columns_names': ['forum'],
            'columns_values': [forum_sh_name],
            'table': 'Post'
        }
        if since != 0:
            larger = {'id': since}
            sql = build_sql_select_all_query(sql_scheme, group='user', what='user', larger=larger, limit=limit)
        else:
            sql = build_sql_select_all_query(sql_scheme, group='user', what='user', limit=limit)

        posts_list_dict = open_sql_all(sql, first=True, is_closing=False)
        posts_list = posts_list_dict['result']
        db = posts_list_dict['db']
        crs = posts_list_dict['cursor']

        mails = []

        for x in posts_list:
            mails.append(x['user'])

        if mails:
            sql_scheme = {
                'columns_names': ['email'],
                'columns_values': mails,
                'table': 'User'
            }
            if since != 0:
                sql = build_sql_select_all_query(sql_scheme, larger={'id': since}, limit=limit, ord_by=' name ',
                                                 is_desc=is_desc, in_set=True)
            else:
                sql = build_sql_select_all_query(sql_scheme, limit=limit, ord_by=' name ', is_desc=is_desc, in_set=True)

            users_res_dict = open_sql_all(sql, first=False, is_closing=False, cursor=crs)
            users_res = users_res_dict['result']

    resp_list = []
    final_resp = make_response(code=code)

    if code == 0 and users_res:
        for res in users_res:
            #usr_details = get_details_user({'user': [res['email'], ]})
            #usr_details = usr_details['response']
            res['subscriptions'] = [] #usr_details['subscriptions']
            res['followers'] = [] #usr_details['followers']
            res['following'] = [] #usr_details['following']
            resp_list.append(res)

    db.close()
    final_resp = {'code': code, 'response': resp_list}
    return final_resp
