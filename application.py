from flask import Flask, jsonify
from flasgger import Swagger
from app import create_app

application = create_app()
Swagger(application)

from mysql.connector import Error as MySQLError

@application.errorhandler(MySQLError)
def handle_mysql_error(error):
    response = {"error": str(error)}
    return jsonify(response), 400


if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0", port=5000)