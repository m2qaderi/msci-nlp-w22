import re
import sys
import gensim
from gensim.models import Word2Vec
import numpy as np
import pandas as pd 
from gensim.models import KeyedVectors
import pickle
from nltk.util import pad_sequence
from keras.preprocessing.text import text_to_word_sequence, Tokenizer
from keras import layers
from keras.layers.embeddings import Embedding
from keras.models import Sequential
import tensorflow as tf
from keras import Input 
from keras.layers import Dense 
from keras.layers import Dropout
from sklearn.feature_extraction.text import CountVectorizer
from keras.layers import Flatten

if __name__ == "__main__":
    file_path = sys.argv[0]

    print("Opening file at path: {}".format(file_path))

    with open(file_path) as f: 
        full_text = f.readlines()

    training = file_path + '/train_ns.csv'
    columns = ['sentence','polarity']
    train_df = pd.read_csv(training, delimiter = "\t", names=columns)

    testing = file_path + '/test_ns.csv'
    test_df = pd.read_csv(testing, delimiter = "\t", names=columns)

    y_train = train_df['sentence']
    y_test = test_df['sentence']

    file_path2 = sys.argv[0]
    model = Word2Vec.load(file_path2)
    embeddings_train = [model.wv[word] for word in train_df]
    embeddings_train = pad_sequences(embeddings_train, maxlen=86, padding='post', truncating='post')

    embeddings_test = [model.wv[word] for word in test_df]
    embeddings_test = pad_sequences(embeddings_test, maxlen=86, padding='post', truncating='post')

    #reluModel
    relu_model = Sequential()
    embedding_layer = Embedding(4,32,input_length=86)
    relu_model.add(embedding_layer)
    relu_model.add(Flatten())
    relu_model.add(Dense(128,activation='relu', name='hiddenLayer'))
    relu_model.add(Dense(2, activation='softmax', name='outputLayer'))
    relu_model.add(Dropout(0.2, input_shape=(60,)))

    relu_model.compile(
        loss='binary_crossentropy',
        optimizer='adam',
        metrics=['accuracy'])

    relu_model.fit(embeddings_train,y_train,batch_size=10)
    pickle.dump(relu_model, open(file_path + '/nn_relu.model.pkl', 'wb'))

    predict_train = (relu_model.predict(embeddings_train)).astype(int)
    predict_test = (relu_model.predict(embeddings_test)).astype(int)
    print('Relu Model Accuracy:')
    print(predict_test)
    relu_model.summary()

    #sigmoid
    sigmoid_model = Sequential()
    embeddingLayer = Embedding(4,32,input_length=86)
    sigmoid_model.add(embeddingLayer)
    sigmoid_model.add(Flatten())
    sigmoid_model.add(Dense(128,activation='sigmoid', name='hiddenLayer'))
    sigmoid_model.add(Dense(2, activation='softmax', name='outputLayer'))
    sigmoid_model.add(Dropout(0.2, input_shape=(60,)))


    sigmoid_model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy'])

    sigmoid_model.fit(embeddings_train,y_train,batch_size=10)
    pickle.dump(sigmoid_model, open(file_path + '/nn_sigmoid.model.pkl', 'wb'))

    predict_train = (sigmoid_model.predict(embeddings_train)).astype(int)
    predict_test = (sigmoid_model.predict(embeddings_test)).astype(int)
    sigmoid_model.summary()
    print('Sigmoid Model Accuracy:')
    print(predict_test)

    # Tanh
    tanh_model = Sequential()
    embeddingLayer = Embedding(4,32,input_length=86)
    tanh_model.add(embeddingLayer)
    tanh_model.add(Flatten())
    tanh_model.add(Dense(128,activation='tanh', name='hiddenLayer'))
    tanh_model.add(Dense(2, activation='softmax', name='outputLayer'))
    tanh_model.add(Dropout(0.2, input_shape=(60,)))


    tanh_model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy'])

    tanh_model.fit(embeddings_train,y_train,batch_size=10)
    pickle.dump(tanh_model, open(file_path + '/nn_tanh.model.pkl', 'wb'))

    predSentientTrain = (tanh_model.predict(embeddings_train)).astype(int)
    predSentientTest = (tanh_model.predict(embeddings_test)).astype(int)
    tanh_model.summary()
    print('Tanh Model Accuracy:')
    print(predict_test)