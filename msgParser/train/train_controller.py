import os, json
from flask import request, Response, jsonify, flash, redirect, url_for, Blueprint
from flask import current_app as app
from werkzeug.utils import secure_filename
from chatbot.nlu_model import train_model

train = Blueprint('train', __name__)

@train.route('/train', methods=['GET', 'POST', 'OPTIONS'])
def index():
    if request.method == 'GET':
        ResponseToSend = {
            "Client IP" : request.remote_addr,
            "User agent" : str(request.user_agent)
        }
        RespData = json.dumps(ResponseToSend, sort_keys=True, indent=4)
        resp = Response(RespData, status=200, mimetype='application/json')
        return resp
    if request.method == 'POST':
        #check for file in post request
        if 'file' not in request.files:
            flash('No file part')
            return redirect(url_for('index'))

        f = request.files['file']
        if f.filename=='':
            flash('No file selected')
            return redirect(url_for('index'))

        #valid file found
        if f:
            #secure_filename ensures to correct any mistakes made by the user while uploading
            filename = secure_filename(f.filename)
            print("File received : {}".format(filename))

            
            filepath = "/".join([os.path.realpath('.'), app.config['UPLOAD_FOLDER'], filename])
            configpath = "/".join([os.path.realpath('.'), app.config['CONFIG_PATH']])
            modelpath = "/".join([os.path.realpath('.'), app.config['MODEL_DIR']])
            f.save(filepath)
            print("File Saved.")

            modeldirec = train_model(filepath, configpath, modelpath)
            print("Training data Successful.")

            # post training completion, store the path of the model trained in app.config
            app.config['MODEL_DIRECTORY'] = modeldirec

            # delete the file received from client
            if os.path.isfile(filepath):
                os.remove(filepath)
                flash("File Removed.") 
            
            ResponseToSend = {
                "Upload Status" : "Sucess",
                "Training Status" : "Success",
                "Removal Status" : "Success"
            }

            RespData = json.dumps(ResponseToSend, sort_keys=True, indent=4)
            resp = Response(RespData, status=201, mimetype='application/json')
            return resp

    if request.method == 'OPTIONS':
        resp = Response(status=200)
        resp.headers['Allow'] = ['GET', 'POST', 'OPTIONS']
        return resp