__author__ = 'kic'
import MySQLdb

from forum_app.settings import DB


def exec_sql(sql):
    database = MySQLdb.connect(user=DB['USER'], host=DB['HOST'], passwd=DB['PASSWORD'], db=DB['NAME'], charset='utf8')
    cursor = database.cursor()

    cursor.execute(sql)

    database.commit()
    database.close()
    return 0


def open_sql(sql):
    database = MySQLdb.connect(user=DB['USER'], host=DB['HOST'], passwd=DB['PASSWORD'], db=DB['NAME'], charset='utf8')
    cursor = database.cursor()

    cursor.execute(sql)
    db_resp = cursor.fetchall()

    result = None
    if db_resp:
        columns = [item[0] for item in cursor.description]
        result = dict(zip(columns, db_resp[0]))

    database.close()
    return result


def build_sql_query(sql_scheme):

    columns_names = ','.join(sql_scheme['columns_names'])

    columns_values = "'" + "','".join(sql_scheme['columns_values']) + "'"
    return sql_scheme['type'] + ' into ' + sql_scheme[
        'table'] + '(' + columns_names + ')' + 'values(' + columns_values + ')'