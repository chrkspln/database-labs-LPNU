import mysql.connector
from flasgger import Swagger
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from app.auth.route import register_routes
from app.setup import Config
import os
from dotenv import load_dotenv
from blocklist import BLOCKLIST

load_dotenv()
jwt = JWTManager()

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
    "security": [
        {
            "Bearer": []
        }
    ]
}

@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_payload):
    return jwt_payload["jti"] in BLOCKLIST


@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return (
        jsonify(
            {"description": "The token has been revoked.", "error": "token_revoked"}
        ),
        401,
    )
db = SQLAlchemy()

def create_app():
    load_dotenv()
    connection = mysql.connector.connect(
        host=os.environ.get('DB_HOST'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        database=os.environ.get('DB_NAME'),
    )

    application = Flask(__name__)
    application.config.from_object(Config)
    application.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
    swagger = Swagger(application, template=swagger_template)
    db.init_app(application)
    register_routes(application)

    create_database(connection)
    with application.app_context():
        create_tables(application)
        populate_data(connection)
        execute_sql_scripts(connection, ['../scripts/cursor.sql', '../scripts/triggers.sql'])

    return application


def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS lab4_auchan")
    cursor.close()


def create_tables(application):
    with application.app_context():
        db.create_all()


def populate_data(connection):
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


def execute_sql_scripts(connection, file_names):
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