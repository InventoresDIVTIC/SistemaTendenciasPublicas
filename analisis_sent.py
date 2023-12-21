import pandas as pd
import nltk 
import numpy as np
import spacy
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import text #for stop_word 

data=pd.read_csv('entrenamiento/IMDB Dataset SPANISH.csv')
columns_remove = ['Unnamed: 0', 'review_en', 'sentiment']
data=data.drop(columns_remove ,axis=1)
#Remove duplicated
data.drop_duplicates(inplace=True)


print(data.value_counts('sentimiento'))
print(' ')
print('nulos')
print(data.isnull().sum())

def clean_text(text):
    # convert text to lowercase
    text = text.lower()

    #Remove URLs
    text=re.sub(r'http:?\S+','',text)

    # Remove punctuation characters
    text = re.sub("[%s]" % re.escape(string.punctuation), " ", text)
    
    # Remove non-ASCII characters, but ncluding Latin characters
    text = re.sub("([^\x00-\x7F\u00C0-\u017F])+", " ", text)
  

    #remove extra spaces and words with less than 2 characters
    filter = [palabra for palabra in text.split() if (len(palabra) > 2 or palabra=='no') and palabra.isalpha() ]
    text = " ".join(filter)
   
    return text
data['review_es_clean'] = data['review_es'].apply(lambda x: clean_text(x))


from nltk.corpus import stopwords
nltk.download('stopwords')
stop=list(stopwords.words("spanish"))

def remove_stopwords(text):
    stopwords_esp = stopwords.words('spanish') 
    words = text.split()
    text= [word for word in words if word not in stopwords_esp]
    return " ".join(text)
data['review_es_clean']=data['review_es_clean'].apply(lambda x: remove_stopwords(x))

from nltk.corpus import stopwords
nltk.download('stopwords')
stop=list(stopwords.words("spanish"))

def remove_stopwords(text):
    stopwords_esp = stopwords.words('spanish') 
    words = text.split()
    text= [word for word in words if word not in stopwords_esp]
    return " ".join(text)
data['review_es_clean']=data['review_es_clean'].apply(lambda x: remove_stopwords(x))

data.head()

columns_remove = ['review_es','review_es_clean']
data=data.drop(columns_remove ,axis=1)

from sklearn.model_selection import train_test_split
train, test = train_test_split(data,test_size=0.30,random_state=42)
x_train,y_train=train['review_es_lemma'],train['sentimiento']
x_test,y_test=test['review_es_lemma'],test['sentimiento']
print(len(x_train),len(x_test))

#Note1: it´s better to use bigram than unigram, but needs GPU.
#Note2: To find a min and a max, you must try several values. Recommendation max_df(0.7-0.9)
tfidf=TfidfVectorizer(ngram_range=(1,2),min_df=0.005,max_df=0.70) 
X_train=tfidf.fit_transform(x_train).toarray()  #y_train no es necesario porque es la salida 
X_test=tfidf.transform(x_test).toarray()  #no toca hacer fit de nuevo ya que tfidf ya hizo fit arriba en train
print("train",X_train.shape)
print("test",X_test.shape) 

import keras
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Convolution1D, AveragePooling1D, Flatten, Dense, Input, MaxPooling1D, Dropout
from sklearn.metrics import classification_report,confusion_matrix

le = LabelEncoder()
y_train_encoded = le.fit_transform(y_train)
y_test_encoded = le.transform(y_test)
print(le.classes_)

modelo = Sequential()
modelo.add(Input(shape=(3488,1)))
modelo.add(Convolution1D(128, kernel_size=3, activation="relu"))
modelo.add(MaxPooling1D(pool_size=(2)))
modelo.add(Dropout(0.5))
modelo.add(Convolution1D(32, kernel_size=3, activation="relu"))
modelo.add(MaxPooling1D(pool_size=(2)))
modelo.add(Dropout(0.5))
modelo.add(Flatten())
modelo.add(Dense(32, activation="relu"))
modelo.add(Dense(1, activation="sigmoid"))

modelo.compile(optimizer="adam", loss="binary_crossentropy",
               metrics=["accuracy","Precision"]
)
modelo.summary()

modelo.fit(X_train, y_train_encoded, validation_batch_size=(X_test,y_test_encoded),epochs=20)
pred = modelo.predict(X_test)
pred_labels = (pred > 0.5).astype(int)

print(classification_report(y_test_encoded, pred_labels))

print("Negative")
print(modelo.predict(tfidf.transform(['Esta película fue una completa pérdida de tiempo. El guion era confuso y la trama carecía de coherencia. Los actores parecían aburridos y poco comprometidos con sus personajes. Definitivamente, una de las peores películas que he visto']).toarray()))
print(modelo.predict(tfidf.transform(['No puedo creer que esta película haya recibido buenas críticas. La trama predecible y los diálogos cliché hicieron que fuera una experiencia aburrida. Además, los efectos especiales eran de mala calidad y la dirección carecía de originalidad' ]).toarray()))
print(modelo.predict(tfidf.transform(['Una película llena de pretensiones. Intentaba ser profunda y reflexiva, pero solo logró aburrirme. Los personajes eran insulsos y no lograron despertar ninguna emoción en mí. No recomendaría perder el tiempo viendo esto' ]).toarray()))
print(modelo.predict(tfidf.transform(['Esta película prometía ser una emocionante aventura, pero se quedó en un intento fallido. Los efectos especiales eran deslumbrantes, pero eso no compensó la falta de desarrollo de la trama y la falta de carisma de los personajes. No vale la pena']).toarray()))
print(modelo.predict(tfidf.transform(['Una película que se autodenomina comedia, pero no hizo que ni siquiera una sonrisa se dibujara en mi rostro. Los chistes eran forzados y los actores parecían estar sobreactuando en todo momento. Evitaría esta película a toda costa' ]).toarray()))

print("Positive")
print(modelo.predict(tfidf.transform(['Esta película es una verdadera joya cinematográfica. El guion es inteligente y conmovedor, manteniéndote enganchado de principio a fin. Los actores entregan interpretaciones excepcionales, y la dirección es impecable. Definitivamente, una película que no te puedes perder']).toarray()))
print(modelo.predict(tfidf.transform(['Una obra maestra del cine. La historia es profundamente emotiva y te hace reflexionar sobre la vida. Los efectos visuales son impresionantes y la banda sonora es cautivadora. Los actores dan vida a personajes memorables y te sumergen por completo en la trama' ]).toarray()))
print(modelo.predict(tfidf.transform(['Una película que te deja sin aliento. La acción es trepidante y las escenas de combate son coreografiadas de manera brillante. Además, el guion inteligente y lleno de giros inesperados te mantiene en vilo hasta el último minuto. Definitivamente, una experiencia cinematográfica inolvidable' ]).toarray()))
print(modelo.predict(tfidf.transform(['Una comedia ingeniosa y refrescante que te hará reír a carcajadas. Los diálogos son hilarantes y los actores tienen una química perfecta. Además, la dirección logra capturar la esencia de la historia de una manera divertida y entretenida. Una película que te dejará de buen humor']).toarray()))
print(modelo.predict(tfidf.transform(['Una película que te transporta a un mundo de fantasía asombroso. Los efectos especiales son impresionantes y te sumergen por completo en ese universo mágico. La historia es conmovedora y los personajes te roban el corazón. Una película que te hace creer en la magia del cine' ]).toarray()))


modelo.save('modelo_imdb_review.h5')

import pickle
with open('modelo_tfidf.pkl', 'wb') as file:
    pickle.dump(tfidf, file)