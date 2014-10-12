__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql
from forum_app.api_packs.forum_api.forum_func import get_forum_response


def create_forum(data):
    name = data['name'].encode("utf-8")
    shn = data['short_name'].encode("utf-8")
    usr = data['user'].encode("utf-8")

    sql_check = "select id,name,short_name,user from Forum where name = '%s' and short_name = '%s' " % (name, shn)
    res = open_sql(sql_check)  # check if exists
    if not res:
        sql = "insert into Forum (name,short_name,user) values('%s','%s','%s')" % (name, shn, usr)
        res = exec_sql(sql)
        if res == 0:
            res = open_sql(sql_check)
        else:
            TODO = None
    resp_dict = get_forum_response(fid=int(res['id']), name=res['name'], short_name=res['short_name'], user=res['user'])

    return flask.jsonify(resp_dict)

