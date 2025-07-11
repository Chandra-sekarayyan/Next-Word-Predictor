Next Word Prediction Web App (LSTM + Flask)

This is an AI-powered web application that predicts the next most probable word in a sentence using a Long Short-Term Memory (LSTM) neural network. It offers real-time predictions with an interactive, user-friendly frontend and a Flask backend.

📌 Features

- 🔠 Predicts the next word based on the typed context
- 📊 Displays top 5 word suggestions with confidence scores
- ⚡ Real-time, dynamic predictions using AJAX (JavaScript Fetch API)
- 🧠 LSTM model trained using Keras and TensorFlow
- 🌐 Responsive frontend with modern glassmorphism UI
- 🔁 Sentence-building interface where suggestions update contextually

🛠️ Technologies Used

- **Python**, **TensorFlow**, **Keras** — model development and training
- **Flask** — lightweight web backend
- **HTML**, **CSS**, **JavaScript** — frontend development
- **Pickle** — to serialize tokenizer and model configuration
- **Google Colab** — training environment with GPU acceleration

📂 Project Structure

```
├── app.py                  # Flask backend API
├── templates/
│   └── index.html          # Main UI page
├── static/
│   ├── style.css           # UI styles (glassmorphism)
│   └── script.js           # JS logic to fetch predictions
├── trained_model.keras     # Trained LSTM model
├── tokenizer_and_max_seq_len.pkl # Tokenizer and sequence metadata
└── README.md
```

🚀 Getting Started

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/nextwordpredictor.git
   cd nextwordpredictor
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask app**  
   ```bash
   python app.py
   ```

4. **Visit the app**  
   Open `http://localhost:5000` in your browser.

🧠 Model Training 

- Train your model using Google Colab (provided notebook)
- Save the `.keras` model and tokenizer `.pkl` file to your working directory
- Load them in `app.py`


💡 Use Cases

- Smart typing and keyboard apps
- AI-powered writing tools
- NLP learning and academic demos


