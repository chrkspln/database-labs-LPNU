import MySQLdb
from flask import jsonify

from app import create_app, db

app = create_app()

@app.errorhandler(MySQLdb.OperationalError)
def handle_mysql_error(error):
    # Extract the message from the SQLAlchemy exception
    response = {
        "error": f"{str(error.orig)}"  # Get the raw message
    }
    return jsonify(response), 400

if __name__ == '__main__':
    app.run(debug=True)