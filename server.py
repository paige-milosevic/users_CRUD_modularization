print('Hello World')
from flask_app import app
from flask_app.controllers.users import User
# from flask_app.controllers import users

if __name__ == "__main__":
    app.run(debug=True)

