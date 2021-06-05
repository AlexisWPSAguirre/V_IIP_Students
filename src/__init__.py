from flask import Flask

app = Flask(__name__, template_folder='views')

# Importando Controllers
from src.controllers import *

def create_app():
    app.run(debug=True)