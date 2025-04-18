# import pandas as pd
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.naive_bayes import MultinomialNB
# import pickle

# data = {
#     "symptoms": [
#         "fever cough fatigue",
#         "headache dizziness nausea",
#         "rash itching redness",
#         "vomiting diarrhea",
#         "chest pain shortness of breath"
#     ],
#     "disease": [
#         "Flu",
#         "Migraine",
#         "Allergy",
#         "Food Poisoning",
#         "Heart Issue"
#     ]
# }
# df = pd.DataFrame(data)
# vectorizer = CountVectorizer()
# X = vectorizer.fit_transform(df["symptoms"])
# y = df["disease"]

# model = MultinomialNB()
# model.fit(X, y)

# pickle.dump(model, open("model.pkl", "wb"))
# pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))




# train_model.py

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Sample dataset (you can later use a larger one from Kaggle)
data = {
    "symptoms": [
        "fever cough fatigue",
        "headache dizziness nausea",
        "rash itching redness",
        "vomiting diarrhea stomach ache",
        "chest pain shortness of breath"
    ],
    "disease": [
        "Flu",
        "Migraine",
        "Allergy",
        "Food Poisoning",
        "Heart Issue"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert symptoms into feature vectors
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["symptoms"])
y = df["disease"]

# Train Naive Bayes model
model = MultinomialNB()
model.fit(X, y)

# Save model and vectorizer
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model and vectorizer saved successfully.")
