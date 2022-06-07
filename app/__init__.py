"""Setup at app startup"""
import os
import sqlalchemy
from flask import Flask
from yaml import load, Loader



def init_connection_engine():
    try:
        variables = load(open("app.yaml"), Loader=Loader)
        env_variables = variables['env_variables']
        for var in env_variables:
            os.environ[var] = env_variables[var]
    except OSError as e:
        print("Make sure you have the app.yaml file setup")
        os.exit()


    if os.environ.get('LOCAL') == 'FALSE':
        print('otwieramy połączenie z online db')
        pool = sqlalchemy.create_engine(
            sqlalchemy.engine.url.URL(
                drivername="mysql+pymysql",
                username=os.environ.get('MYSQL_USER'),
                password=os.environ.get('MYSQL_PASSWORD'),
                database=os.environ.get('MYSQL_DB'),
                host=os.environ.get('MYSQL_HOST')
            )
        )
    else:
        print('otwieramy locala')
        pool = sqlalchemy.create_engine(
        "mysql+pymysql://root:Test1234@localhost/todolist",
        connect_args= dict(host='localhost', port=3306)
        )
    return pool


app = Flask(__name__)
db = init_connection_engine()


from app import routes
