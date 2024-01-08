import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn import metrics
import spacy

# Cargar el modelo de Spacy para español
nlp = spacy.load('es_core_news_sm')

# Leer el archivo CSV con las columnas 'review_es' y 'sentimiento'
data = pd.read_csv('entrenamiento/IMDB Dataset SPANISH.csv')

# Dividir el conjunto de datos en entrenamiento y prueba
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Preprocesamiento de texto con Spacy
def preprocess_text(text):
    doc = nlp(text)
    return ' '.join([token.lemma_ for token in doc if not token.is_punct and not token.is_stop])

# Aplicar preprocesamiento a los conjuntos de entrenamiento y prueba
train_data['processed_text'] = train_data['review_es'].apply(preprocess_text)
test_data['processed_text'] = test_data['review_es'].apply(preprocess_text)

# Crear un clasificador con un modelo de bolsa de palabras y Naive Bayes
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Entrenar el modelo con los datos de entrenamiento
model.fit(train_data['processed_text'], train_data['sentimiento'])

# Predecir el conjunto de prueba
predicted_sentiments = model.predict(test_data['processed_text'])

# Medir la precisión del modelo
accuracy = metrics.accuracy_score(test_data['sentimiento'], predicted_sentiments)
print(f'Precisión del modelo: {accuracy:.2f}')

# Imprimir ejemplos de predicciones en el conjunto de prueba
print("\nEjemplos de predicciones en el conjunto de prueba:")
for i in range(5):
    print(f'Texto: {test_data["review_es"].iloc[i]}')
    print(f'Predicción: {predicted_sentiments[i]}')
    print(f'Etiqueta real: {test_data["sentimiento"].iloc[i]}\n')

# Clasificar un nuevo texto
new_text = "Este producto es excelente, lo recomiendo totalmente."
preprocessed_new_text = preprocess_text(new_text)
prediction = model.predict([preprocessed_new_text])[0]
print(f'Clasificación del nuevo texto: {prediction}')

import joblib

joblib.dump(model, 'modelo_entrenado.pkl')