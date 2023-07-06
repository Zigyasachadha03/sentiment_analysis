# Sentiment Analysis Project

This repository contains code and resources for a Sentiment Analysis project. The goal of this project is to analyze the sentiment (positive or negative) of text data using machine learning techniques and provide predictions based on trained models.

## Dataset

The dataset used for this project is obtained from Kaggle's Twitter dataset, available at [this link](https://www.kaggle.com/datasets/kazanova/sentiment140). The dataset consists of tweets labeled with sentiment, where positive tweets are labeled as 4 and negative tweets as 0.

## Approach

The project follows the following approach:

### Data Preprocessing

The dataset is preprocessed to clean the text, remove noise, and transform the data into a suitable format for training the models.

### Naive Bayes

Initially, a Naive Bayes classifier is implemented to classify the sentiment of the text data. This serves as a baseline model.

### Deep Learning Models

To improve the performance, deep learning models are implemented using TensorFlow and Keras. The following models are trained and evaluated:

- Simple Neural Network
- LSTM (Long Short-Term Memory)
- GRU (Gated Recurrent Unit)
- Bi-LSTM (Bidirectional LSTM)

### Model Evaluation

The trained models are evaluated using appropriate evaluation metrics such as accuracy, precision, recall, and F1 score to assess their performance.

### Model Selection

Based on the evaluation results, the Bi-LSTM model is selected as the final model due to its good accuracy and performance.

### Model Saving

The trained Bi-LSTM model is saved to be used for deployment.

### Web Application

A Flask-based web application is built to provide an interface for users to input text data and obtain sentiment predictions using the deployed Bi-LSTM model.

## Usage

To use this project, follow these steps:

1. Clone the repository:
' git clone https://github.com/your-username/sentiment-analysis-project.git '

2. Download the Twitter dataset from Kaggle's website and place it in the appropriate folder within the repository.

3. Install the required dependencies specified in the `requirements.txt` file.

4. Preprocess the dataset and train the models using the provided code.

5. Evaluate the trained models and select the Bi-LSTM model for deployment.

6. Save the selected Bi-LSTM model.

7. Run the Flask web application to deploy the model:
'python app.py'

8. Access the web application through the provided URL and enter the text data to obtain sentiment predictions.

## Conclusion

This Sentiment Analysis project demonstrates the process of training and deploying machine learning models to analyze the sentiment of text data. Starting from a Naive Bayes classifier, the project progresses to deep learning models and concludes with the deployment of a Bi-LSTM model using a Flask web application.

Feel free to explore the code, experiment with different models and techniques, and adapt the project for your own use cases.
