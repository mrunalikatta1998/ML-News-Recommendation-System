import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.metrics.pairwise import cosine_similarity as cs
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.multiclass import OneVsRestClassifier
from newsrecapis.dataprep import PrepTrainingData, get_tfidf, encode_labels

import os

from sklearn.svm import SVC

print("Current Working Directory:", os.getcwd())


from sklearn.preprocessing import StandardScaler
def train_svc(X, y, filename):
    y = encode_labels(y)  # Assuming you have a function for encoding labels
    print("Encoded labels")
    # Preprocessing: Scaling the features
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    print("x scaled")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print("train test split")
    # Creating the SVM model
    model = OneVsRestClassifier(SVC(kernel='linear', max_iter=5000, tol=1e-3))
    print("model created")
    # Fitting the model with training data
    model.fit(X_train, y_train)
    print("model trained")
    # Making a prediction on the test set
    prediction = model.predict(X_test)
    print("predictions made")
    # Evaluating the model
    print('Precision is {}'.format(precision_score(y_test, prediction, average='macro')))
    print('Recall is {}'.format(recall_score(y_test, prediction, average='macro')))
    print('F1:', f1_score(y_test, prediction, average='macro'))


    try:
        with open(filename, 'wb') as f:
            pickle.dump(model, f)
    except Exception as e:
        print(f"Error saving model to {filename}: {e}")

    print(f"Model saved to {filename}")


def train_svc_model():
    print("Training model...")
    df = PrepTrainingData()
    print("Data preprocessed...")
    print("tfid generating...")
    X_tfidf = get_tfidf(df['text'])
    print("tfid generated...")
    train_svc(X_tfidf, df['combined_categories'], "newsrecapis/MLModels/picklefilesofmodels/svm_model_combinedcat.pkl")
    train_svc(X_tfidf, df['category_level_1'], "newsrecapis/MLModels/picklefilesofmodels/svm_model_cat1.pkl")
    train_svc(X_tfidf, df['category_level_2'], "newsrecapis/MLModels/picklefilesofmodels/svm_model_cat2.pkl")
