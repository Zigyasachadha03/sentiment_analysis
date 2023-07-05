from flask import Flask, render_template, request, redirect
import tensorflow as tf
import os
from tensorflow import keras

app = Flask(__name__)


# Get the path to the model file
model_path = "C:\\Users\\zigya\\OneDrive\\Desktop\\Intern Projects\\Sentiment Anlaysis\\saved models\\model_Bi_LSTM"

# Load the model
model = keras.models.load_model(model_path)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    sentence = request.form['sentence']

    # Preprocess the sentence (if required)
    # ...

    # Perform the prediction
    prediction = model.predict([sentence])[0]
    probability = prediction[0]
    result = 'Positive' if probability >= 0.5 else 'Negative'

    html_page = 'positive_result.html' if result == 'Positive' else 'negative_result.html'
    return render_template(html_page, sentence=sentence, probability=probability, result=result)


@app.route('/goback')
def go_back():
    return redirect('/')

if __name__ == '__main__':
    app.run()
