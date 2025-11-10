from flask import jsonify
from flasgger import Swagger
from app import create_app
import MySQLdb

application = create_app()
swagger = Swagger(application)

@application.errorhandler(MySQLdb.OperationalError)
def handle_mysql_error(error):
    response = {"error": f"{str(error.orig)}"}
    return jsonify(response), 400

if __name__ == '__main__':
    application.run(debug=True)