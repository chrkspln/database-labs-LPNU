from flasgger import Swagger
from flask import jsonify
from app import create_app, swagger_template, swagger_config

application = create_app()
Swagger(application, template=swagger_template, config=swagger_config)

from mysql.connector import Error as MySQLError

@application.errorhandler(MySQLError)
def handle_mysql_error(error):
    response = {"error": str(error)}
    return jsonify(response), 400


if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0", port=5000)