from flask import Flask, redirect, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'

debug = DebugToolbarExtension(app)