import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.metrics.pairwise import cosine_similarity as cs
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.multiclass import OneVsRestClassifier
from newsrecapis.dataprep import PrepTrainingData, get_tfidf, encode_labels

import os

print("Current Working Directory:", os.getcwd())


from sklearn.preprocessing import StandardScaler
def train_lr(X, y, filename):
    y = encode_labels(y)
    
    #Splitting the dataset with stratification to preserve class distribution
    X_train_lr, X_test_lr, y_train_lr, y_test_lr = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Scaling the features
    scaler = StandardScaler()
    X_train_lr = scaler.fit_transform(X_train_lr)
    X_test_lr = scaler.transform(X_test_lr)

    # Logistic Regression with optimized parameters
    model = OneVsRestClassifier(
        LogisticRegression(solver='lbfgs', C=1.0, max_iter=200, tol=1e-3, class_weight='balanced')
    )

    # Fitting the model with training data
    model.fit(X_train_lr, y_train_lr)

    # Making predictions on the test set
    prediction = model.predict(X_test_lr)

    # Evaluating the model
    print('Precision is {}'.format(precision_score(y_test_lr, prediction, average='macro')))
    print('Recall is {}'.format(recall_score(y_test_lr, prediction, average='macro')))
    print('F1:', f1_score(y_test_lr, prediction, average='macro'))


    try:
        with open(filename, 'wb') as f:
            pickle.dump(model, f)
    except Exception as e:
        print(f"Error saving model to {filename}: {e}")

    print(f"Model saved to {filename}")


def train_lr_model():
    print("Training model...")
    df = PrepTrainingData()
    df['text'] = df['text'].astype(str).fillna('')
    print("Data preprocessed...")
    print("tfid generating...")
    X_tfidf = get_tfidf(df['text'])
    print ("tfid generated...", X_tfidf)
    
    print("tfid generated...")
    train_lr(X_tfidf, df['combined_categories'], "newsrecapis/MLModels/picklefilesofmodels/lr_model_combinedcat.pkl")
    train_lr(X_tfidf, df['category_level_1'], "newsrecapis/MLModels/picklefilesofmodels/lr_model_cat1.pkl")
    train_lr(X_tfidf, df['category_level_2'], "newsrecapis/MLModels/picklefilesofmodels/lr_model_cat2.pkl")
