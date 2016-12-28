#!/usr/bin/python
#-*- coding: utf-8 -*-
from flask import Flask, request
import os
app = Flask(__name__, static_folder='static') 


@app.route('/static/<path:path>')
def static_proxy(path):
    return app.send_static_file(path)

@app.route('/upload', methods=['POST'])
def upgrade_upload():
    try: 
        originfile = request.files['file']
        print originfile.filename
        packagepath = "/opt"
        if not os.path.exists(packagepath):
            os.makedirs(packagepath)
        destfile = os.path.join(packagepath, originfile.filename)                                                                             
        with file(destfile, 'wb') as f:
            f.write(originfile.read())
        return ("success",200)
    except Exception as e:
        return ("error", 400)
  
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
