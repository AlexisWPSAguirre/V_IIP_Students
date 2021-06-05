from flask import session
from src import app
app.secret_key = 'sha512'
session