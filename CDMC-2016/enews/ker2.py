import keras.preprocessing.text
import numpy as np
import pandas as pd
np.random.seed(1337)  # for reproducibility
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM
from sklearn.metrics import (precision_score, recall_score,f1_score, accuracy_score,mean_squared_error,mean_absolute_error)
from sklearn import metrics
from sklearn.metrics import roc_auc_score
from keras.utils.np_utils import to_categorical
from sklearn.cross_validation import train_test_split
from keras.layers import Dropout
from keras.layers import LSTM
from keras.layers.convolutional import Convolution1D
from keras.layers.convolutional import MaxPooling1D
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from theano.tensor.shared_randomstreams import RandomStreams
# fix random seed for reproducibility
np.random.seed(7)
srng = RandomStreams(7)

print("Loading")

traindata = pd.read_csv('eNews_2016_Train.csv', header=None)


x = traindata.iloc[:,0]
y = traindata.iloc[:,1]



tk = keras.preprocessing.text.Tokenizer(nb_words=7000, filters=keras.preprocessing.text.base_filter(), lower=True, split=",")
tk.fit_on_texts(x)
X_train = tk.texts_to_sequences(x)


X_train=np.array(X_train)


y_train = np.array(y)


batch_size = 64
max_len = 1000
print "max_len ", max_len
print('Pad sequences (samples x time)')

X_train = sequence.pad_sequences(X_train, maxlen=max_len)
#X_test = sequence.pad_sequences(X_test, maxlen=max_len)

y_train= to_categorical(y_train)
#y_test = to_categorical(y_test)


max_features = 7000
model = Sequential()
print('Build model...')
embedding_vecor_length = 32


model = Sequential()
model.add(Embedding(max_features, embedding_vecor_length, input_length=max_len))
model.add(Dropout(0.2))
model.add(LSTM(100))
model.add(Dropout(0.2))
model.add(Dense(5))
model.add(Activation('softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam',metrics=['accuracy'])
print(model.summary())

#model.compile(loss='binary_crossentropy', optimizer='adam',metrics=['accuracy'])
#print(model.summary())

model.fit(X_train, y_train, batch_size=batch_size, nb_epoch=25,
          validation_split=0.20, shuffle=True)

#print('Test score:', score)
#print('Test accuracy:', acc)


