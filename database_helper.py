import sqlalchemy

LOCAL= 'FALSE'
MYSQL_USER= 'useradmin@mysqlservernamegroup1'
MYSQL_PASSWORD= 'test1234!'
MYSQL_DB= 'todolist'
MYSQL_HOST=  'mysqlservernamegroup1.mysql.database.azure.com'
driver= 'mysql+pymysql'

def init_connection_engine():
    if LOCAL == 'FALSE':
        print('Try connect to online DB')
        pool = sqlalchemy.create_engine(
            sqlalchemy.engine.url.URL(
                drivername='mysql+pymysql',
                username=MYSQL_USER,
                password=MYSQL_PASSWORD,
                database=MYSQL_DB,
                host=MYSQL_HOST
            )
        )
    else:
        print('Try connect to local DB')
        pool = sqlalchemy.create_engine(
            "mysql+pymysql://root:Test1234@localhost/todolist"
        )
    return pool

def fetch_todo() -> dict:
    db = init_connection_engine()
    conn = db.connect()
    query_results = conn.execute("Select * from tasks;").fetchall()
    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "id": result[0],
            "task": result[1],
            "status": result[2]
        }
        todo_list.append(item)
    return todo_list
