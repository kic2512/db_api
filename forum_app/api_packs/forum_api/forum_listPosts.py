from forum_app.api_packs.db_queries.queries import build_sql_select_all_query, open_sql, open_sql_all
from forum_app.api_packs.forum_api.forum_details import get_details_forum
from forum_app.api_packs.make_response.make_response import make_response
from forum_app.api_packs.thread_api.thread_details import get_details_thread
from forum_app.api_packs.user_api.user_details import get_details_user

__author__ = 'kic'


def get_forum_posts_list(data):
    code = 0
    posts_list = []

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
            'table': 'Post'
        }
        if since != 0:
            larger = {'date': since}
            sql = build_sql_select_all_query(sql_scheme, is_desc, limit, larger)
        else:
            sql = build_sql_select_all_query(sql_scheme, is_desc, limit)

        posts_list = open_sql_all(sql)

    resp_keys = ['date', 'forum', 'id', 'isApproved', 'isDeleted', 'isEdited', 'isHighlighted', 'isSpam', 'message',
                 'parent', 'thread', 'user', 'likes', 'dislikes', 'points']

    resp_dict = []
    final_resp = make_response(code=code)

    if code == 0 and posts_list:
        for res in posts_list:
            resp_values = [str(res['date']), res['forum'], res['id'], bool(res['isApproved']), bool(res['isDeleted']),
                           bool(res['isEdited']), bool(res['isHighlighted']), bool(res['isSpam']), res['message'],
                           res['parent'], res['thread'], res['user'], res['likes'], res['dislikes'],
                           res['points']]
            resp_dict.append(make_response(resp_keys, resp_values, code)['response'])

        if 'thread' in related:
            for x in resp_dict:
                x['thread'] = get_details_thread({'thread': [x['thread'], ]})['response']

        if 'forum' in related:
            for x in resp_dict:
                x['forum'] = get_details_forum({'forum': [x['forum'], ]})['response']

        if 'user' in related:
            for x in resp_dict:
                x['user'] = get_details_user({'user': [x['user'], ]})['response']

        final_resp = {'code': code, 'response': resp_dict}

    return final_resp
