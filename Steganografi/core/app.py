#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import time
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('home.html')



if __name__ == "__main__":
    print('oh hello')
    #time.sleep(5)
    app.run(host='127.0.0.1', port=1337)
