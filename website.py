#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 16:25:31 2021

@author: dhaval
"""

from flask import Flask, render_template

app = Flask(__name__,template_folder='/Users/dhaval/Desktop/Prerna/templates',static_folder='/Users/dhaval/Desktop/Prerna/static')

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about/')
def about():
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True)
    
    