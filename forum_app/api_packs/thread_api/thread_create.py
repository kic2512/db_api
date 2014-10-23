from forum_app.api_packs.user_api.user_details import get_details_user

__author__ = 'kic'
import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, build_sql_insert_query, build_sql_select_all_query
from forum_app.api_packs.make_response.make_response import make_response


def create_thread(data):
    code = 0
    forum = data['forum']
    title = data['title']

    isclosed = data['isClosed']

    date = data['date']
    message = data['message']
    slug = data['slug']

    email = data['user']

    if 'isDeleted' in data:
        isdeleted = data['isDeleted']
    else:
        isdeleted = 'False'

    sql_scheme = {
        'columns_names': ['title'],
        'columns_values': [title],
        'table': 'Thread'
    }

    sql_check = build_sql_select_all_query(sql_scheme)

    res = open_sql(sql_check)  # check if exists

    if not res:
        sql_scheme = {
            'columns_names': ['forum', 'title', 'isClosed', 'user', 'date', 'message', 'slug', 'isDeleted'],
            'columns_values': [forum, title, int(isclosed), email, date, message, slug, int(isdeleted)],
            'table': 'Thread'
        }
        sql = build_sql_insert_query(sql_scheme)
        exec_message = exec_sql(sql)

        if exec_message == 0:
            res = open_sql(sql_check)
        else:
            code = 4
    keys = ['id', 'date', 'forum', 'isClosed', 'isDeleted', 'message', 'slug', 'title', 'user']
    values = [res['id'], str(res['date']), res['forum'], bool(res['isClosed']), bool(res['isDeleted']), res['message'],
              res['slug'], res['title'], res['user']]

    resp_dict = make_response(keys, values, code)

    return flask.jsonify(resp_dict)
