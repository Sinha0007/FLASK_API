import sqlite3
DATABASE_NAME = "games.db"


def get_db():
    conn = sqlite3.connect("games.db")
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS games(
                #id INTEGER PRIMARY KEY AUTOINCREMENT,
                #price REAL NOT NULL,
				#rate INTEGER NOT NULL
            )
            """,
        """
insert into games values(1, 'john', '200', 50)"""
    ]

    db = get_db()
    cursor = db.cursor()
    for table in tables:
     cursor.execute("""CREATE TABLE IF NOT EXISTS games(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
				price REAL NOT NULL,
				rate INTEGER NOT NULL
            )
            """)
    db.commit
    res=cursor.execute("insert into games values(1, 'john', '200', 50)")
    db.commit 
    print(res.fetchone())