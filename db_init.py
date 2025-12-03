from app import create_app
from app.db_import import db
from app.auth.model import *

from app.__init__ import create_tables, populate_data, execute_sql_scripts
from app.setup import Config
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def init_database():
    print("[init_db] Connecting to DB...")

    # Create proper Flask app
    app = create_app()

    connection = mysql.connector.connect(
        host=os.environ["DB_HOST"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"]
    )

    print("[init_db] Creating tables...")
    with app.app_context():
        create_tables(app)

    print("[init_db] Populating data...")
    populate_data(connection)

    print("[init_db] Executing scripts...")
    execute_sql_scripts(connection, ['scripts/cursor.sql', 'scripts/triggers.sql'])

    connection.close()
    print("[init_db] Done.")


if __name__ == "__main__":
    init_database()
