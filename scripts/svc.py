# Author: Lucía María Álvarez Crespo (GitHub: @luciamariaalvarezcrespo)
# Last modified: 26/06/2023
# Description: Support Vector Machine
# Python version: 3.10.6

import os
import re
import numpy as np
import pandas as pd
import random_undersampling
import joblib
import fasttext
import fasttext.util
from nltk.tokenize import TweetTokenizer
from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline

def preprocess_tweet(tweet):
    """
    Preprocesses a tweet by applying various text transformations.

    Args:
        tweet (str): The tweet to be preprocessed.

    Returns:
        str: The preprocessed tweet.

    """
    if not isinstance(tweet, str) or tweet is None:
        return None
    
    tweet = tweet.lower()
    tweet = re.sub(r'\n', '', tweet)
    tweet = re.sub(r'http://t.co/[a-zA-Z0-9]+', 'http://t.co', tweet)
    tweet = re.sub(r'@\w+', '', tweet)
    tweet = re.sub(r'::', '', tweet)
    tweet = re.sub(r'#(\w+)', r'\1', tweet)
    tweet = re.sub(r'(.)\1{2,}', r'\1', tweet)
    if not tweet.strip():
        return None
    return tweet

def generate_sentence_embeddings(tweet, fasttext_model):
    """
    Generates sentence embeddings using FastText.

    Args:
        tweet (str): The tweet to be preprocessed.
        fasttext_model: The FastText model used for generating embeddings.

    Returns:
        str: The sentence embedding.

    """
    tokenizer = TweetTokenizer(preserve_case=False, reduce_len=True)
    tokens = tokenizer.tokenize(tweet)
    embeddings = [fasttext_model.get_word_vector(word) for word in tokens]
    sentence_embedding = sum(embeddings) / len(embeddings)
    return ' '.join(str(val) for val in sentence_embedding)

# Load the dataset for class 0 (non-misogynous toots)
df_toots = pd.read_csv(os.path.dirname(__file__) + "/../corpus/toots.csv")
df_toots['content'] = df_toots['content'].apply(preprocess_tweet)
df_toots = df_toots.dropna(subset=['content'])  # Remove rows with empty toots
X_0 = df_toots['content']
y_0 = pd.Series([0] * len(X_0))

# Load the dataset for class 1 (misogynous tweets)
df_tweets = pd.read_csv(os.path.dirname(__file__) + "/../corpus/tweets.csv")
df_tweets['content'] = df_tweets['content'].apply(preprocess_tweet)
df_tweets = df_tweets.dropna(subset=['content'])  # Remove rows with empty tweets
X_1 = df_tweets['content'] 
y_1 = pd.Series([1] * len(X_1))

# Combine the datasets
X = pd.concat([X_0, X_1], ignore_index=True)
y = pd.concat([y_0, y_1], ignore_index=True)

# Download FastText model and load it
fasttext.util.download_model('gl', if_exists='ignore')  # Galician
fasttext_model = fasttext.load_model('cc.gl.300.bin')

# Define the machine learning classifier
classifier = SVC()

# Define the pipeline for BoW representation and classifier
bow_pipeline = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('select_k_best', SelectKBest(score_func=chi2)),
    ('clf', classifier)
])

# Generate sentence embeddings
sentence_embeddings = X.apply(lambda tweet: generate_sentence_embeddings(tweet, fasttext_model))
sentence_embeddings = np.array(sentence_embeddings.tolist())

# Split the dataset into training and testing sets, being 70% for training and 30% for testing
X_train, X_test, y_train, y_test = train_test_split(sentence_embeddings, y, test_size=0.3)

# Define the parameter grid
param_grid = {
    'clf__kernel': ['poly'],
    'clf__C': [1]
}

# Perform Grid Search to find the best model
grid_search = GridSearchCV(estimator=bow_pipeline, param_grid=param_grid, scoring='f1', cv=10)
grid_search.fit(X_train, y_train)
best_model = grid_search.best_estimator_
FILENAME = 'best_model_SVM.pkl'
joblib.dump(best_model, FILENAME)

# Evaluate the best model
y_pred = best_model.predict(X_test)
f1 = f1_score(y_test, y_pred, average='weighted')
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
accuracy = accuracy_score(y_test, y_pred)

# Print the results
print('Support Vector Machine')
print(f'Best F1 Score: {f1:.4f}')
print(f'Precision: {precision:.4f}')
print(f'Recall: {recall:.4f}')
print(f'Accuracy: {accuracy:.4f}')

# UNDERSAMPLING TRAINING SET

# Perform undersampling
X_res, y_res = random_undersampling.random_undersampling(X, y)

# Define the pipeline for BoW representation and classifier
bow_pipeline = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('select_k_best', SelectKBest(score_func=chi2)),
    ('clf', classifier)
])

# Generate sentence embeddings
sentence_embeddings = X_res.apply(lambda tweet: generate_sentence_embeddings(tweet, fasttext_model))
sentence_embeddings = np.array(sentence_embeddings.tolist())

# Split the dataset into training and testing sets, being 70% for training and 30% for testing
X_train, X_test, y_train, y_test = train_test_split(sentence_embeddings, y_res, test_size=0.3)

# Perform Grid Search to find the best model
grid_search = GridSearchCV(estimator=bow_pipeline, param_grid=param_grid, scoring='f1', cv=10)
grid_search.fit(X_train, y_train)
best_model = grid_search.best_estimator_
FILENAME = 'best_model_SVM_RUS.pkl'
joblib.dump(best_model, FILENAME)

# Evaluate the best model
y_pred = best_model.predict(X_test)
f1 = f1_score(y_test, y_pred, average='weighted')
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
accuracy = accuracy_score(y_test, y_pred)

# Print the results
print('Random Forest Classifier with Random Undersampling')
print(f'Best F1 Score: {f1:.4f}')
print(f'Precision: {precision:.4f}')
print(f'Recall: {recall:.4f}')
print(f'Accuracy: {accuracy:.4f}')