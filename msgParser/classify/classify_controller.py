import os, json
from flask import request, Response, jsonify, flash, redirect, url_for, Blueprint, abort
from flask import current_app as app
from werkzeug.utils import secure_filename
from chatbot.nlu_model import run_model

classify = Blueprint('classify', __name__)



@classify.route('/classify', methods = ['POST'])
def index():
    if request.method == 'POST':
        if not request.json or not 'text' in request.json:
            abort(400)

        content = request.json
        text = content['text']

        # call run_model to run the chatbot on the text received from the client
        bot_OP = run_model(app.config['MODEL_DIRECTORY'], text)

        # Entities [] holds the entity names extracted by the bot from the input sentence
        Entities = []
        for obj in bot_OP["entities"]:
            Entities.append({
                obj["entity"] : obj["value"]
            })

        ResponseToSend = {
            "intent" : bot_OP["intent"]["name"],
            "entities" : Entities
        }

        RespData = json.dumps(ResponseToSend, sort_keys=True, indent=4)
        resp = Response(RespData, status=200, mimetype='application/json')
        return resp