from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_cors import CORS
from flask_jwt_extended import JWTManager  # Import JWTManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECURITY_PASSWORD_SALT'] = 'my_precious_two'
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'  # Replace with your JWT secret key
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# Initialize CORS with your app
CORS(app)

# Initialize JWTManager with your app
jwt = JWTManager(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "practicesession3@gmail.com"
app.config['MAIL_PASSWORD'] = "gpap kwxz sujc qxie"
mail = Mail(app)

from flaskblog import routes  # Assuming your routes are defined in the flaskblog package
