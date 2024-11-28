import mysql.connector
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.auth.route import register_routes
from app.setup import Config
import os

db = SQLAlchemy()

# Establishing connection without specifying database initially
connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='chrkspln'
)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    register_routes(app)

    create_database()  # Ensure the database exists
    with app.app_context():
        create_tables(app)  # Create necessary tables within app context
        populate_data()  # Populate tables with data

    return app


def create_database():
    global connection  # Ensure persistence of the connection
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS lab4_auchan")

    # Reconnect to the newly created database
    connection.database = 'lab4_auchan'
    cursor.close()


def create_tables(app):
    with app.app_context():
        db.create_all()  # SQLAlchemy creates the tables


def populate_data():
    sql_file_path = os.path.abspath('data.sql')

    # Corrected the path check
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

    # Only close the connection at the end
    connection.close()
