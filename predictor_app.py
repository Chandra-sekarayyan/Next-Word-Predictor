import os
from flask import Flask, render_template, request, jsonify
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle

app = Flask(__name__)
model = tf.keras.models.load_model("D:\\next word predictor\\trained_model.keras")

with open('D:\\next word predictor\\tokenizer_and_max_seq_len.pkl', 'rb') as f:
    loaded_data = pickle.load(f)

tokenizer = loaded_data['tokenizer']
max_seq_len = loaded_data['max_seq_len']

def load_resources():
    global model, tokenizer, max_seq_len
    print("Loading model and tokenizer...")
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
        print(f"Model loaded from {MODEL_PATH}")

        with open(TOKENIZER_PATH, 'rb') as f:
            loaded_data = pickle.load(f)
            tokenizer = loaded_data['tokenizer']
            max_seq_len = loaded_data['max_seq_len']
        print(f"Tokenizer and max_seq_len loaded from {TOKENIZER_PATH}")
        print(f"Max sequence length: {max_seq_len}")
    except Exception as e:
        print(f"Error loading resources: {e}")
        
with app.app_context():
    load_resources()

def predict_next_word(seed_text):
    if not model or not tokenizer or not max_seq_len:
        print("Model, tokenizer, or max_seq_len not loaded.")
        return {"error": "Prediction resources not available."}

    token_list = tokenizer.texts_to_sequences([seed_text.lower()])[0]
    token_list = pad_sequences([token_list], maxlen=max_seq_len - 1, padding='pre')
    
    predicted_probabilities = model.predict(token_list, verbose=0)[0]

    sorted_indices_desc = np.argsort(predicted_probabilities)[::-1]

    top_predictions = {}
    for i in range(5):
        idx = sorted_indices_desc[i]
        word = tokenizer.index_word.get(idx, '[UNK]') 
        probability = float(predicted_probabilities[idx] * 100)
        top_predictions[word] = f"{probability:.2f}%"

    return top_predictions

@app.route('/')
def index():
    return render_template('n_w_predictor.html')

@app.route('/predict', methods=['POST'])
def api_predict():
    data = request.get_json()
    seed_text = data.get('text', '')

    if not seed_text:
        return jsonify({"error": "No text provided"}), 400

    predictions = predict_next_word(seed_text)
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True)