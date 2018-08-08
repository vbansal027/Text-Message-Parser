import os
from flask import Flask, jsonify, Blueprint, request, Response, abort, json
from smsParser.train.train_controller import train
from smsParser.classify.classify_controller import classify

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(classify)
    app.register_blueprint(train)

    # app.config.from_mapping(
    #     SECRET_KEY = 'dev'
    # )
    app.config.from_object('smsParser.settings')
    # app.config.from_pyfile('config.cfg', silent=True)
    # if test_config is None:
    #     app.config.from_pyfile('config.cfg', silent=True)
    # else:
    #     app.config.from_mapping(test_config)
    

    @app.route('/home')
    def home():
        #print(app.config['FLASK_ENV'])
        print(app.config['SECRET_KEY'])
        print(os.path.realpath('.'))
        #print(app.url_map) -----> This is to print the list of registered routes with the app.
        if request.method == 'GET':

            ResponseToSend = {
                "About" : "Hello User",
                "User Agent" : str(request.user_agent),
                "Client IP" : request.remote_addr   
            }

            RespData = json.dumps(ResponseToSend, indent=4, sort_keys=True)
            return Response(RespData, status=200, content_type='application/json')
        else :
            abort(400)

    return app