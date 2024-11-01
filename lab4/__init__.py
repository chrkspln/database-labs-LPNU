import mysql.connector
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from lab4.auth.route import register_routes
from lab4.setup import Config
import os
import sys

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    register_routes(app)
    create_database()
    create_tables(app)
    populate_data()
    return app


def create_database():
    connection = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='chrkspln',
        database='lab4_auchan'
    )
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS lab4_auchan")
    cursor.close()
    connection.close()


def create_tables(app):
    with app.app_context():
        db.create_all()


def populate_data():
    sql_file_path = os.path.abspath('..sql/data.sql')
    if os.path.exists('..sql/data.sql'):
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='chrkspln',
            database='lab4_auchan'
        )
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