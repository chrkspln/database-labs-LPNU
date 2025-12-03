# init_db.py

import os
import mysql.connector
from dotenv import load_dotenv
from flask import Flask
from app.__init__ import db, create_tables, populate_data, execute_sql_scripts
from app.auth import model
from app.setup import Config

load_dotenv()


def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get('DB_HOST'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        database=os.environ.get('DB_NAME')
    )


def init_database():
    """Run full DB initialization: tables, data, scripts."""
    print("[init_db] Connecting to DB...")

    connection = get_db_connection()

    # Temporary Flask app for SQLAlchemy
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    print("[init_db] Creating tables...")
    with app.app_context():
        create_tables(app)

    print("[init_db] Populating data from data.sql...")
    populate_data(connection)

    print("[init_db] Executing SQL scripts...")
    execute_sql_scripts(connection, [
        'scripts/cursor.sql',
        'scripts/triggers.sql'
    ])

    connection.close()
    print("[init_db] Done.")


if __name__ == "__main__":
    init_database()
