import mysql.connector
from flasgger import Swagger
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from app.auth.route import register_routes
from app.setup import Config
from app.auth import model
import os
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Auchan API",
        "description": "API docs for auchan stores",
        "version": "1.0.0",
    },
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "JWT Authorization header using the Bearer scheme. Example: 'Bearer {token}'"
        }
    },
    "security": [{"Bearer": []}]
}

def get_db_connection():
    """Connect to the RDS instance using env variables."""
    return mysql.connector.connect(
        host=os.environ.get('DB_HOST'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        database=os.environ.get('DB_NAME')
    )


def create_app():
    # Flask app setup
    application = Flask(__name__)
    application.config.from_object(Config)
    db.init_app(application)
    register_routes(application)

    return application


def create_tables(application):
    """Create tables via SQLAlchemy if they don't exist."""
    with application.app_context():
        db.create_all()


def populate_data(connection):
    """Populate DB with initial data from data.sql if it exists."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    sql_file_path = os.path.join(base_dir, '..', 'data.sql')
    if not os.path.exists(sql_file_path):
        return

    cursor = connection.cursor()
    with open(sql_file_path, 'r') as sql_file:
        sql_text = sql_file.read()
        sql_statements = sql_text.split(';')
        for stmt in sql_statements:
            stmt = stmt.strip()
            if stmt:
                try:
                    cursor.execute(stmt)
                    connection.commit()
                except mysql.connector.Error as err:
                    print(f"[populate_data] Error executing SQL: {err}")
                    connection.rollback()
    cursor.close()


def execute_sql_scripts(connection, file_names):
    """Execute arbitrary SQL scripts for triggers, cursors, etc."""
    cursor = connection.cursor()
    for file_name in file_names:
        file_path = os.path.abspath(file_name)
        if not os.path.exists(file_path):
            continue

        print(f"[execute_sql_scripts] Executing: {file_name}")
        with open(file_path, 'r') as sql_file:
            sql_text = sql_file.read()
            sql_statements = sql_text.split(';')
            for stmt in sql_statements:
                stmt = stmt.strip()
                if stmt:
                    try:
                        cursor.execute(stmt)
                        connection.commit()
                    except mysql.connector.Error as err:
                        print(f"[execute_sql_scripts] Error executing SQL: {err}")
                        print(f"Statement: {stmt}")
                        connection.rollback()
    cursor.close()
