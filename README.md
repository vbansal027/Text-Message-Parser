# Message Parser

This is a nlp based, Flask application, written in Python, using the rasa-nlu natural language processing engine. The app requires a structured data input to be trained from and then prepares a trained nlp model from it. Subsequently, using the trained model, it will extract and return the *intent* and *entities* (refer to rasa-nlu) from the sentence fed into it.

## Technologies Used
* [Rasa-nlu](https://nlu.rasa.com/)
* [Python 3](https://docs.python.org/3/)
* [Flask](http://flask.pocoo.org/docs/1.0/)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Things you need, to install the software, are all included in the *requirements* file. All you need to do is simply pip install the requirements with the command listed below.
*It is suggested to setup a virtual environment for your Flask application and then perform the requirement installation*

```
pip install -r requirements
```

### Installing

##### Set up a virtual environment
[Click here](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b) to install virtualenvironment if you don't already have it.

```
mkdir myproject
cd myproject
python3 -m venv venv
```
##### Activate the environment
```
source venv/bin/activate
```

To deactivate
```
deactivate
```
##### Installing requirements in the environment
```
pip install -r requirements
```
RasaNLU, in this project, is running on a backend of spaCy and scikit-learn, so do not forget to install medium sized language model for english language and link it. Do this by the following commands.
```
python3 -m spacy download en_core_web_md
python3 -m spacy link en_core_web_md en
```
## Starting up the server

To start the server you simply need to run the runServer.sh script. By default it will start the server in production, but to change the environment simply change the FLASK_ENV to development.

## Configuring the app

App is configured using settings.py which includes the data, configuration and model directory paths used by nlu_model.py.

A detailed description of alternate ways to configure your flask app can be found [here](http://flask.pocoo.org/docs/1.0/config/).

Currently the app saves everything in the project folder itself.
The training .json file uploaded is by default deleted post training completion.
A demo of the training file can be found [here](https://github.com/RasaHQ/rasa_nlu/blob/master/data/examples/rasa/demo-rasa.json).

Trained models are saved in msgParser.classify.models

## Training and Testing

* The app exposes POST http request API to post training data and test sentence.
* The training data has to be sent as file, using *multipart/form* type POST request.
* The test sentence has to be of type **_application/json_**.
* The return will be of type **_application/json_** consisting of keys: entities, intent. 

## Authors

* **Vidur Khanna**
* **Vaibhav Bansal**
