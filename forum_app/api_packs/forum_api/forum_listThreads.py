__author__ = 'kic'

from forum_app.api_packs.db_queries.queries import build_sql_select_all_query, open_sql, open_sql_all
from forum_app.api_packs.forum_api.forum_details import get_details_forum
from forum_app.api_packs.make_response.make_response import make_response
from forum_app.api_packs.thread_api.thread_details import get_details_thread
from forum_app.api_packs.user_api.user_details import get_details_user


def get_forum_threads_list(data):
    code = 0
    thread_list = []

    forum_sh_name = data.get('forum')[0]

    since = data.get('since', [0, ])[0]

    limit = data.get('limit', [0, ])[0]

    sort_by = data.get('sort', 'flat')

    related = data.get('related', [0, ])

    is_desc = 0
    order_by = data.get('order', 'desc')
    if 'desc' in order_by:
        is_desc = 1

    sql_scheme = {
        'columns_names': ['short_name'],
        'columns_values': [forum_sh_name],
        'table': 'Forum'
    }

    sql_check = build_sql_select_all_query(sql_scheme)

    res = open_sql(sql_check)  # check if exists

    if not res:
        code = 5
    else:
        sql_scheme = {
            'columns_names': ['forum'],
            'columns_values': [forum_sh_name],
            'table': 'Thread'
        }
        if since != 0:
            larger = {'date': since}
            sql = build_sql_select_all_query(sql_scheme, is_desc=is_desc, limit=limit, larger=larger, ord_by=' date ')
        else:
            sql = build_sql_select_all_query(sql_scheme, is_desc=is_desc, limit=limit, ord_by=' date ')

        thread_list = open_sql_all(sql)

    resp_keys = ['id', 'date', 'forum', 'isClosed', 'isDeleted', 'message', 'slug', 'title', 'user']

    resp_dict = []
    final_resp = make_response(code=code)

    if code == 0 and thread_list:
        for res in thread_list:
            thread_data = get_details_thread({'thread': [res['id'], ]})['response']
            resp_dict.append(thread_data)

        if 'forum' in related:
            for x in resp_dict:
                x['forum'] = get_details_forum({'forum': [x['forum'], ]})['response']

        if 'user' in related:
            for x in resp_dict:
                x['user'] = get_details_user({'user': [x['user'], ]})['response']

        final_resp = {'code': code, 'response': resp_dict}

    return final_resp