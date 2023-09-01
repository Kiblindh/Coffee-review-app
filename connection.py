
def connection(db):
    import sqlite3
    con = sqlite3.connect(db)
    cursor = con.cursor()
    return cursor


