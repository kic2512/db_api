__author__ = 'kic'
import MySQLdb
import mysql.connector
from forum_app.settings import DB


def exec_sql(sql, multi=False):
    database = None
    try:
        database = mysql.connector.connect(user=DB['USER'], host=DB['HOST'], passwd=DB['PASSWORD'], db=DB['NAME'],
                                           charset='utf8', connection_timeout=15)

        cursor = database.cursor()
        if not multi:
            cursor.execute(sql)
            result = cursor.lastrowid
        else:
            cursor.execute("START TRANSACTION")
            for s in sql:
                cursor.execute(s)
            cursor.execute("COMMIT")
            result = cursor.lastrowid

        database.commit()
        database.close()
    except mysql.connector.Error as err:
        result = -1
        if database:
            database.close()

    return result


def open_sql(sql):
    result = None
    database = None
    try:
        database = mysql.connector.connect(user=DB['USER'], host=DB['HOST'], passwd=DB['PASSWORD'], db=DB['NAME'],
                                           charset='utf8', connection_timeout=15)

        cursor = database.cursor()
        cursor.execute(sql)
        db_resp = cursor.fetchall()

        if db_resp:
            columns = [item[0] for item in cursor.description]
            result = dict(zip(columns, db_resp[0]))
        database.close()
    except mysql.connector.Error as err:
        result = -1
        if database:
            database.close()
    return result


def open_sql_all(sql):
    result = []
    database = None
    try:
        database = mysql.connector.connect(user=DB['USER'], host=DB['HOST'], passwd=DB['PASSWORD'], db=DB['NAME'],
                                           charset='utf8', connection_timeout=15)
        cursor = database.cursor()
        cursor.execute(sql)
        db_resp = cursor.fetchall()

        if db_resp:
            columns = [item[0] for item in cursor.description]
            for x in db_resp:
                result.append(dict(zip(columns, x)))
        database.close()
    except mysql.connector.Error as err:
        result = -1
        if database:
            database.close()

    return result


def build_sql_insert_query(sql_scheme):
    col_dict = dict(zip(sql_scheme['columns_names'], sql_scheme['columns_values']))
    exists_values = dict((k, v) for k, v in col_dict.items() if col_dict[k])

    columns_names = ','.join(exists_values)
    # columns_values = [" '%s' " % x for x in sql_scheme['columns_values'] if x]
    columns_values = [" '%s' " % v for (k, v) in exists_values.items()]
    columns_values = ','.join(columns_values)

    return 'insert into ' + sql_scheme['table'] + '(' + columns_names + ')' + 'values(' + columns_values + ')'


def build_sql_update_query(sql_scheme):
    a = dict(zip(sql_scheme['columns_names'], sql_scheme['columns_values']))
    b = ' , '.join(" %s='%s' " % (k, v) for k, v in a.items())
    condition = [" %s = '%s' " % (k, v) for k, v in sql_scheme['condition'].items()]
    con_str = ' and '.join(condition)
    return 'update ' + sql_scheme['table'] + ' set ' + b + ' where ' + con_str


def build_sql_select_all_query(sql_scheme, is_desc=0, limit=0, larger=None, group=None, what=' * ', ord_by=' id ',
                               in_set=None):
    # columns_names = ','.join(sql_scheme['columns_names'])

    desc = ''
    str_lim = ''
    c = ''
    str_by = ord_by
    str_group = ''
    if is_desc:
        desc = ' desc '
    if limit:
        str_lim = " limit  %s " % limit
    columns_values = ["'%s'" % x for x in sql_scheme['columns_values']]

    if group:
        str_group = " group by %s " % group

    a = dict(zip(sql_scheme['columns_names'], columns_values))
    if not in_set:
        b = ' and '.join(' %s=%s ' % (k, v) for k, v in a.items())
    else:
        b = str(sql_scheme['columns_names'][0]) + ' in (' + ','.join(' %s ' % x for x in columns_values) + ')'
    if larger:
        c = ' and ' + ' and '.join(" %s>='%s' " % (k, v) for k, v in larger.items())

    return 'select ' + what + ' from ' + sql_scheme[
        'table'] + ' where ' + b + c + str_group + ' order by ' + str_by + desc + str_lim