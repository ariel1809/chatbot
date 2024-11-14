from flask import Flask, request, jsonify, render_template
from mlearning.models import predict_class, get_response

# Créer une instance de l'application Flask
app = Flask(__name__)

# Route pour la page du chatbot
@app.route('/chatbot')
def chat():
    return render_template('chat.html')

# Route pour la page à propos
@app.route('/about')
def about():
    return render_template('about.html')

# Route pour prédire l'intention
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Lire les données JSON envoyées par l'utilisateur
    message = data.get('message')
    
    if not message:
        return jsonify({'error': 'No message provided'}), 400
    
    # Prédire la classe
    predicted_tag = predict_class(message)
    bot_response = get_response(predicted_tag)
    
    return jsonify({'response': bot_response})