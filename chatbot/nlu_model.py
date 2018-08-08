from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter
from rasa_nlu import config

def train_model(data_path, config_path, model_path):
    training_data = load_data(data_path)
    trainer = Trainer(config.load(config_path))
    trainer.train(training_data)
    model_directory = trainer.persist(model_path)
    return model_directory

def run_model(model_directory, text):
    interpreter = Interpreter.load(model_directory)
    return (interpreter.parse(text))

# if __name__=='__main__':
#     dt_path = './data/examples/rasa/demo-rasa.json'
#     con_path = './sample_configs/config_spacy.yml'
#     model_dir = './projects/'
#     text = 'looking for a chinese restaurant'

#     model_directory = train_model(dt_path, con_path, model_dir)
#     resp = run_model(model_directory, text)
#     print(resp)