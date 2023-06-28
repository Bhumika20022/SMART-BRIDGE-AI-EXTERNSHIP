from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk #natural lnaguage toolkit
import re #regural expression
#for stop word
nltk.download('stopwords')
from nltk.corpus import stopwords
#for stemminh
from nltk.stem.porter import PorterStemmer
import tensorflow as tf
from tensorflow.keras.models import load_model
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.layers import Dense,LSTM,Embedding
from tensorflow.keras.models import Sequential
import pickle
import joblib
vocab_size=10000
sent_length=20
model = load_model('churn.h5')
ps = PorterStemmer()
app = Flask(__name__, static_folder="static")


@app.route('/')
def demo():
    return render_template('predict.html')

@app.route('/predict',methods=['POST'])
def prediction():
    typ = str(request.form['type'])
    op = typ
    op = re.sub('[^a-zA-Z]', ' ', op)
    op = op.lower()
    op = op.split()
    op = [ps.stem(word) for word in op if word not in set(stopwords.words('english'))]
    op = ' '.join(op)
    one_hot_repr = [one_hot(op, vocab_size)]
    pad_doc = pad_sequences(one_hot_repr, padding='pre', maxlen=sent_length)
    pred2 = model.predict(pad_doc)
    if (pred2 > 0.5):
        fraud = 'positive'
    else:
        fraud = 'negetive'
    return render_template('predict.html',output='Our model predicts that the news is  {}'.format(fraud))



if __name__ == '__main__':
    app.run(debug=True)
