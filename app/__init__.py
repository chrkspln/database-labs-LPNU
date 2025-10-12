import mysql.connector
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.auth.route import register_routes
from app.setup import Config
import os

db = SQLAlchemy()

connection = mysql.connector.connect(
    host=os.environ.get('DB_HOST'),
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASSWORD'),
    database=os.environ.get('DB_NAME'),
)

def create_app():
    application = Flask(__name__)
    application.config.from_object(Config)
    db.init_app(application)
    register_routes(application)

    create_database()
    with application.app_context():
        create_tables(application)
        populate_data()
        execute_sql_scripts(['../scripts/cursor.sql', '../scripts/triggers.sql'])

    return application


def create_database():
    global connection
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS lab4_auchan")
    cursor.close()


def create_tables(application):
    with application.app_context():
        db.create_all()


def populate_data():
    sql_file_path = os.path.abspath('data.sql')
    if os.path.exists(sql_file_path):
        cursor = connection.cursor()
        with open(sql_file_path, 'r') as sql_file:
            sql_text = sql_file.read()
            sql_statements = sql_text.split(';')

            for statement in sql_statements:
                statement = statement.strip()
                if statement:
                    try:
                        cursor.execute(statement)
                        connection.commit()
                    except mysql.connector.Error as error:
                        print(f"Error executing SQL statement: {error}")
                        connection.rollback()

        cursor.close()
        connection.close()


def execute_sql_scripts(file_names):
    cursor = connection.cursor()
    for file_name in file_names:
        file_path = os.path.abspath(file_name)
        if os.path.exists(file_path):
            print(f"Executing SQL statement: {file_name}")
            with open(file_path, 'r') as sql_file:
                sql_text = sql_file.read()
                sql_statements = sql_text.split(';')
                for statement in sql_statements:
                    statement = statement.strip()
                    if statement:
                        try:
                            cursor.execute(statement)
                            connection.commit()
                        except mysql.connector.Error as error:
                            print(f"Error executing SQL statement: {error}")
                            print(f"SQL statement: {statement}")
                            connection.rollback()

    cursor.close()
    connection.close()