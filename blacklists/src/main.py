from .blueprints.blacklist_blueprint import blacklist_blueprint
from .errors.errors import ApiError
from .models.blacklist_entry import db
from flask import Flask, jsonify
from dotenv import load_dotenv
import os

app = Flask(__name__)
app_context = app.app_context()
app_context.push()

load_dotenv('.env.development')

# Configure the database
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT")
db_name = os.environ.get("DB_NAME")
db_uri = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Initialize SQLAlchemy

# Create the database tables
with app.app_context():
    db.create_all()

# Register blueprint
app.register_blueprint(blacklist_blueprint)


@app.errorhandler(ApiError)
def handle_exception(err):
    response = {
        "msg": err.description
    }
    return jsonify(response), err.code
