# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 10:36:58 2020

@author: DELL
"""
from flask import Flask,render_template,request

import pickle
import numpy as np

model = pickle.load(open('price1.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods =['post'])
def login():
    moisture = request.form['moisture']
    volatile_nature = request.form['volatile_nature']
    alkalines = request.form['alkalines']
    state = request.form['state']
    if (state=="NewYork"):
        s1,s2 = 0.0,1.0
    if (state=="California"):
        s1,s2 = 0.0,0.0
    if (state=="Florida"):
        s1,s2 = 1.0,0.0
        
    total = [[int(s1),int(s2),int(moisture),int(volatile_nature),int(alkalines)]]
    print(total)
    y_pred = model.predict(total)
    return render_template("index.html",prediction_text = y_pred)


if __name__ == '__main__':
    app.run(debug = True)