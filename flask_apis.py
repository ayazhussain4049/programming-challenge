# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 22:19:14 2021

@author: Ayaz
"""


from flask import Flask,jsonify,send_file
import os
from generate_objects import generate_file,get_file_stats




app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/generate_file')
def file_generator():
    """API for generating and downloading a file with random strings i.e., alphabateical,integers,
    alphanumeric and real numbers """
    try:
        ###if file is generated
        if(generate_file('random_objects.txt')):
            ###sending file and status success code.
            #return {}
           return send_file('random_objects.txt', as_attachment=True,cache_timeout=0)
        
        else:
            return {"Error":"Failed to generate file!!"},403
    except Exception as error:
        # print(error)
        return {'Error':error},403




@app.route('/file_stats')
def file_stats():
    """Returns the file stats, i.e., number of different string types in file."""
    try:
        ###getting stats of the file
        file_stats=get_file_stats('random_objects.txt')
        if(file_stats is not None):
            return jsonify(file_stats),200
        
        else:
            return {"Error":"File stats not found."},403
    except Exception as error:
        # print(error)
        return {'Error':error},403








@app.route("/")
def home_view():
        return "<h1>Welcome to Flask Service.</h1>\n\n<h2>Service for generating random file.\n http://127.0.0.1:5000/generate_file</h2>\n\n<h2>Service to get file stats. http://127.0.0.1:5000/file_stats</h2>"




if __name__=="__main__":
    port=os.environ.get("PORT",5000)
    app.run(port=port,debug=True)
    

   









