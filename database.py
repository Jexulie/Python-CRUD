import sqlite3
from sqlite3 import Error

DB_PATH = './storage.db'

def readyDatabase():
    try:
        conn = sqlite3.connect(DB_PATH)
        table = createTable()
        if table == True:
            print('Connected to Database')
        else:
            print('Database Error')
    except Error as e:
        print(e)
    finally:
        conn.close()

def createTable():
    SQL = """
    CREATE TABLE IF NOT EXISTS ARTICLES
    (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        TITLE TEXT NOT NULL,
        CONTENT TEXT NOT NULL,
        ENTRY_DATE DATE
    );
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute(SQL)
        return True
    except Error as e:
        return e
    finally:
        conn.close()

def findOne(id):
    SQL = f"""SELECT * FROM ARTICLES WHERE ID = {id}"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute(SQL)
        return cur.fetchall()
    except Error as e:
        return e
    finally:
        conn.close()

def findAll():
    SQL = f"""SELECT * FROM ARTICLES"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute(SQL)
        return cur.fetchall()
    except Error as e:
        return e
    finally:
        conn.close()

def insertOne(title, content):
    SQL = f"""
    INSERT INTO ARTICLES (TITLE, CONTENT, ENTRY_DATE) 
    VALUES(?,?, DATETIME('now'));
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        article = (title, content)
        cur.execute(SQL, article)
        return True
    except Error as e:
        return e
    finally:
        conn.close()

def updateOne(id, newTitle=None, newContent=None):
    if newTitle is None:
        SQL = f"""
        UPDATE ARTICLES
        SET CONTENT = '{newContent}'
        WHERE ID = {id}
        """
    elif newContent is None:
        SQL = f"""
        UPDATE ARTICLES
        SET TITLE = '{newTitle}'
        WHERE ID = {id}
        """
    else:
        SQL = f"""
        UPDATE ARTICLES
        SET TITLE = '{newTitle}',
            CONTENT = '{newContent}'
        WHERE ID = {id}
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute(SQL)
        return True
    except Error as e:
        return e
    finally:
        conn.close()

def removeOne(id):
    SQL = f"""DELETE FROM ARTICLES WHERE ID = {id}"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute(SQL)
        return True
    except Error as e:
        return e
    finally:
        conn.close()