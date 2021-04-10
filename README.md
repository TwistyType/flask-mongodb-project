# Flask REST API application

A flask REST API implementation hosted on mongoDB. MongoDB is hosted on a cluster via the MongoDB Atlas service. 

- Implements URL endpoints for `/register`, `/login` and for `/template/<template_id>`.
- REST API methods are implemented easily in flask through the `flask_restful` package.
- MongoDB is integrated into Python using `flask_mongoengine`
- Passwords are hashed and stored in the DB through `flask_bcrypt` package
- Access tokens are generated via `flask_jwt_extended` package.

Run in powershell: 
1. `$env:ENV_FILE_LOCATION='.env'`	    (in order to set up JWT secret)
2. `$env:FLASK_APP="app.py"`		    (for flask run command)
3. `pip install -r requirements.txt`	(to install requirements to run application)
