import psycopg2

def create_db():
    dbconn = psycopg2.connect(dbname = "post")
    cursor = dbconn.cursor()
    f = open("schema.sql")
    sqlcode = f.read()
    cursor.execute(sqlcode)
    dbconn.commit()
    cursor.close()

def create_post(name, content):
    dbconn = psycopg2.connect(dbname = "post")
    cursor = dbconn.cursor()
    cursor.execute("INSERT INTO posts(name, content) VALUES(%s, %s)", (name, content))
    dbconn.commit()
    cursor.close()

def get_posts():
    dbconn = psycopg2.connect(dbname = "post")
    cursor = dbconn.cursor()
    cursor.execute("SELECT * FROM posts")
    post = cursor.fetchall()
    return post

