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


def open_sql_all(sql):
    database = MySQLdb.connect(user=DB['USER'], host=DB['HOST'], passwd=DB['PASSWORD'], db=DB['NAME'], charset='utf8')
    cursor = database.cursor()
    cursor.execute(sql)
    db_resp = cursor.fetchall()

    result = []
    if db_resp:
        columns = [item[0] for item in cursor.description]
        for x in db_resp:
            result.append(dict(zip(columns, x)))
    database.close()
    return result


def build_sql_insert_query(sql_scheme):

    col_dict = dict(zip(sql_scheme['columns_names'], sql_scheme['columns_values']))
    exists_values = dict((k, v) for k, v in col_dict.items() if col_dict[k])

    columns_names = ','.join(exists_values)
    #columns_values = [" '%s' " % x for x in sql_scheme['columns_values'] if x]
    columns_values = [" '%s' " % v for (k, v) in exists_values.items()]
    columns_values = ','.join(columns_values)

    return 'insert into ' + sql_scheme['table'] + '(' + columns_names + ')' + 'values(' + columns_values + ')'


def build_sql_update_query(sql_scheme):

    a = dict(zip(sql_scheme['columns_names'], sql_scheme['columns_values']))
    b = ' , '.join(" %s='%s' " % (k, v) for k, v in a.items())
    condition = [" %s = '%s' " % (k, v) for k, v in sql_scheme['condition'].items()]
    con_str = ' and '.join(condition)
    return 'update ' + sql_scheme['table'] + ' set ' + b + ' where ' + con_str


def build_sql_select_all_query(sql_scheme, is_desc=0, limit=0, larger=None, group=None):

    #columns_names = ','.join(sql_scheme['columns_names'])

    desc = ''
    str_lim = ''
    c = ''
    str_group = ''
    if is_desc:
        desc = 'desc'
    if limit:
        str_lim = " limit  %s " % limit
    columns_values = ["'%s'" % x for x in sql_scheme['columns_values']]

    if group:
        str_group = " group by %s " % group

    a = dict(zip(sql_scheme['columns_names'], columns_values))
    b = ' and '.join(' %s=%s ' % (k, v) for k, v in a.items())
    if larger:
        c = ' and ' + ' and '.join(" %s>='%s' " % (k, v) for k, v in larger.items())

    return 'select * from ' + sql_scheme['table'] + ' where ' + b + c + str_group +' order by id ' + desc +  str_lim