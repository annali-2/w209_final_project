from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import regex as re
import json
import altair as alt
import matplotlib.pyplot as plt
from ast import literal_eval

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')
   
@app.route('/states')
def states():
   return render_template('states.html')

@app.route('/species')
def species():
   return render_template('species.html')

@app.route('/things_to_do')
def things_to_do():
   return render_template('things_to_do.html')


# home page - main page users will come too
if __name__ == '__main__':
   app.run()