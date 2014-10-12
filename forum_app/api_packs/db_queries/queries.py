__author__ = 'kic'
import MySQLdb

from forum_app.settings import DB


def exec_sql(sql):
    database = MySQLdb.connect(user=DB['USER'], host=DB['HOST'], passwd=DB['PASSWORD'], db=DB['NAME'])
    cursor = database.cursor()

    cursor.execute(sql)

    database.commit()
    database.close()
    return 0


def open_sql(sql):
    database = MySQLdb.connect(user=DB['USER'], host=DB['HOST'], passwd=DB['PASSWORD'], db=DB['NAME'])
    cursor = database.cursor()

    cursor.execute(sql)
    db_resp = cursor.fetchall()

    result = None
    if db_resp:
        columns = [item[0] for item in cursor.description]
        result = dict(zip(columns, db_resp[0]))

    database.close()
    return result
