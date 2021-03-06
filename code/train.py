from stanfordcorenlp import StanfordCoreNLP
from nltk.corpus import wordnet as wn
from googletrans import Translator
import nltk
from nltk.stem import WordNetLemmatizer
l = WordNetLemmatizer()
import json
import pickle

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import random

#Empty list for words, classes and documents
words=[]
classes = []
doc = []
#Ignore certain letters
ignore = ['?', '!', '-','/','\'']
#Load the dataset
data = open('intents.json').read()
intents = json.loads(data)


for intent in intents['intents']:
    for pattern in intent['patterns']:

        #tokenize each word
        w = nltk.word_tokenize(pattern)
        temp = []
        temp.extend(w)
        for every in w:
            syn = wn.synsets(every)
            if len(syn) > 0:
                syn = syn[0].lemma_names()
                if len(syn) < 5:
                    syn_len = len(syn)
                else:
                    syn_len = 5
            
                for i in range(syn_len):
                    t = syn[i].replace("_"," ")
                    t = nltk.word_tokenize(t)
                    temp.extend(t)
            
        words.extend(temp)
        doc.append((temp, intent['tag']))

        # add tags to classes
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# lemmaztize and remove duplicates
temp = []
for w in words:
    if w not in ignore:
        temp.append(l.lemmatize(w.lower()))

#sort words and classes
words = sorted(list(set(temp)))
classes = sorted(list(set(classes)))

#create files for words and classes
pickle.dump(words,open('words.pkl','wb'))
pickle.dump(classes,open('classes.pkl','wb'))

# create our training data
training = []

# create an empty array for our output
output_empty = [0] * len(classes)

# training set, bag of words for each sentence
for d in doc:
    # initialize our bag of words
    bag = []
    # list of tokenized words for every tag stored in documents
    pattern = d[0]
    # lemmatize the words in pattern
    temp = []
    for w in pattern:
        temp.append(l.lemmatize(w.lower()))
        
    pattern = temp
    
    # append 1 (true) if word found and 0 (false) if not found in that particular tag
    for w in words:
        if w in pattern:
            bag.append(1) 
        else:
            bag.append(0)
    
    out = list(output_empty)
    #out is '1' for words with current tag
    out[classes.index(d[1])] = 1
    
    training.append([bag, out])


# shuffle the training data
random.shuffle(training)
training = np.array(training)

# create train and test lists. X - patterns, Y - intents
train_x = list(training[:,0])
train_y = list(training[:,1])


# Create model - 3 layers. First layer 128 neurons, second layer 64 neurons and 3rd output layer contains number of neurons
# equal to number of intents to predict output intent with softmax
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Compile model. Stochastic gradient descent with Nesterov accelerated gradient gives good results for this model
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

#fitting and saving the model 
hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
model.save('model.h5', hist)

print("model created")
