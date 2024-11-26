import json
import pickle
import random

# Charger le modèle et l'encodeur de labels
with open('chatbot_model.pkl', 'rb') as f:
    pipeline = pickle.load(f)

with open('label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

# Charger les réponses depuis le fichier intents.json
with open('intents.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

intents = data['intents']
responses = {}
for intent in intents:
    responses[intent['tag']] = intent['responses']

# Fonction pour prédire la classe
def predict_class(text):
    predicted = pipeline.predict([text])
    return label_encoder.inverse_transform(predicted)[0]

# Fonction pour obtenir la réponse
def get_response(tag):
    return random.choice(responses[tag])