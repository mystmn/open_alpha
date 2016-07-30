import sqlite3 as sql
from flask import g, Flask

app = Flask(__name__)

conn = {
    'db': "models/account_holder/database.db",
    'table': 'account_holder',
    'limit': 20,  # Default Limit
    'desc': 'ORDER BY {} DESC'.format('id'),  # SELECT * FROM tablename ORDER BY column DESC LIMIT 1;
}

def insert_account_holder(email, username, phone, password):
    with sql.connect(conn['db']) as con:
        con.cursor().execute(
            "INSERT INTO account_holder(email,username,phone,password) VALUES (?,?,?,?)",
            (email, username, phone, password))
        con.commit()
    con.close()


def select_account_holder(params=(), limit=()):
    s = "SELECT "
    n = "LIMIT "

    with sql.connect(conn['db']) as con:
        cur = con.cursor()

        if params == ():
            # result = cur.execute("SELECT * FROM {}".format(TABLE, limit))
            s += "* FROM "
        else:
            s += "{} FROM ".format(params)

        if limit == ():
            s += "{} {}".format(str(conn['table']), n + str(conn['limit']))
        else:
            s += "{} {}".format(str(conn['table']), n + str(limit))

        result = cur.execute(s).fetchall()

    con.close()
    return result
