from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_restful import Api
from database.db import initialize_db
from resources.routes import initialize_routes

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')

api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# app.config['MONGODB_SETTINGS'] = {
#     'host': 'mongodb://localhost/user-details'
# }

app.config['MONGODB_SETTINGS'] = {
    'host': "enter_host_here"
}


initialize_db(app)
initialize_routes(api)

if __name__ == '__main__':
    app.run(debug=True)
