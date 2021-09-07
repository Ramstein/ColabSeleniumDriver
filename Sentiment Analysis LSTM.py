# required imports

from keras.layers.core import Activation, Dense, Dropout, SpatialDropout1D
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM
from keras.models import Sequential
from keras.preprocessing import sequence


from sklearn.model_selection import train_test_split

import collections
import matplotlib.pyplot as plt
import nltk
import numpy as np
import os
import random

DATA_DIR_TRAIN = r'C:\Users\Ramstein\PycharmProjects\ColabDriver'
DATA_DIR_TEST = r'C:\Users\Ramstein\PycharmProjects\ColabDriver'
maxlen = 0
word_freqs = collections.Counter()
num_recs = 0

nltk.download('punkt')

ftrain = open(os.path.join(DATA_DIR_TRAIN, 'umich-sentiment-train.txt'), 'rb')

for line in ftrain:
    label, sentence = line.strip().split(b'\t')  # This means that all data read from the file is returned as bytes objects, not str. You cannot then use a string in a containment test:
    words = nltk.word_tokenize(sentence.decode('ascii', 'ignore').lower())

    '''finding the maximum number of word in a sentence in our training corpus'''
    if len(words) > maxlen:
        maxlen = len(words)
    '''finding the number of unique words in our corpus'''
    for word in words:
        word_freqs[word] += 1

    num_recs += 1
ftrain.close()

print('maximum number of word in a sentence in our training corpus: ', maxlen)
print('number of unique words in our corpus: ', len(word_freqs))
print('----------------word_freqs-----------------\n', word_freqs)
print('Number of senteces: ', num_recs)


'''setting our vocabulary size to 2002. This is 2000 words from our vocabulary and UNK, PAD'''
MAX_FEATURES = 2000
MAX_SENTENCE_LENGTH = 40

'''creating Lookup tables which will allow us to lookup an index given the word and the word given the index'''
vocab_size = min(MAX_FEATURES, len(word_freqs)) + 2
word2index = {x[0]: i+2 for i, x in enumerate(word_freqs.most_common(MAX_FEATURES))}
word2index['PAD'] = 0
word2index['UNK'] = 1

index2word = {v:k for k, v in word2index.items()}


print('------------word2index------------\n', word2index)
print('------------index2word-------------\n', index2word)


'''converting our input sequences to word index sequences, padding them to the MAX_SEQUENCE_LENGTH words'''
x = np.empty((num_recs), dtype=list)
y = np.empty((num_recs))

i = 0

ftrain = open(os.path.join(DATA_DIR_TRAIN, 'umich-sentiment-train.txt'), 'rb')
for line in ftrain:
    label, sentence = line.strip().split(b'\t')
    words = nltk.word_tokenize(sentence.decode('ascii', 'ignore').lower())
    seqs = []
    for word in words:
        if word in word2index:
            seqs.append(word2index[word])
        else:
            seqs.append(word2index['UNK'])

    x[i] = seqs
    y[i] = int(label)
    i += 1
ftrain.close()

x = sequence.pad_sequences(x, maxlen=MAX_SENTENCE_LENGTH)


'''splitting the dataset'''
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)

# print('x[i]: ', x[i] )
# print('y[i]: ', y[i] )

print('x: \n', x, '\n y:\n', y)
print('xtrain: ', xtrain, '\nytrain: ', ytrain, '\nxtest: ', xtest, '\nytest: ', ytest)


'''compiling model using binary_crossentropy loss function since it predicts a binary value'''

# value of these hyperparameters were tuned experimentally over saveral runs
EMBEDDING_SIZE = 128
HIDDEN_LAYER_SIZE = 64
BATCH_SIZE = 128
NUM_EPOCHS = 10

# model definition
model = Sequential()
model.add(Embedding(vocab_size, EMBEDDING_SIZE, input_length=(MAX_SENTENCE_LENGTH)))
model.add(SpatialDropout1D(rate=0.2))
model.add(LSTM(HIDDEN_LAYER_SIZE, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# training the network
history = model.fit(xtrain, ytrain, batch_size=BATCH_SIZE, epochs=NUM_EPOCHS, validation_data=(xtest, ytest))

# '''plotting garphs'''
# plt.plot(211)
# plt.title('Accuracy')
# plt.plot(history.history['acc'], color='g', label='train')
# plt.plot(history.history['val_acc'], color='b', label='validation')
# plt.legend(loc='best')
#
# plt.subplot(212)
# plt.title('loss')
# plt.plot(history.history['loss'], color='g', label='train')
# plt.plot(history.history['val_loss'], color='b', label='validation')
# plt.legend(loc='best')
#
# plt.tight_layout()
# plt.show()



'''Evaluating the model'''
score, acc = model.evaluate(xtest, ytest, batch_size=BATCH_SIZE)
print('Test score: %.3f, accuracy: %.3f' %(score, acc))

for i in range(50):
    idx = np.random.randint(len(xtest))
    xtest_temp = xtest[idx].reshape(1, MAX_SENTENCE_LENGTH)
    ytest_temp = ytest[idx]
    ypred = model.predict(xtest_temp)[0][0]

    sent = " ".join([index2word[x] for x in xtest_temp[0].tolist() if x != 0])
    print("%.0f\t%d\t%s" % (ypred, ytest_temp, sent))


