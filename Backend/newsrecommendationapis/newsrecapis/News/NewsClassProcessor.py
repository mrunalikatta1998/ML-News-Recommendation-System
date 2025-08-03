from newsrecapis.News.fetchnews import fetch_news_article, get_newsText
from newsrecapis.dataprep import get_tfidf
import pickle


def get_newsWithClass(modelName):
    print(modelName)
    if modelName == 'lr':
        return get_newsWithClass_lr()
    elif modelName == 'svm':
        return get_newsWithClass_svm()
    elif modelName == 'nb':
        return get_newsWithClass_nb()

def get_newsWithClass_nb():
    model = None

    with open('newsrecapis/MLModels/picklefilesofmodels/nb_model_cat1.pkl', 'rb') as f:
        model = pickle.load(f)

    vectorizer = None
    with open("newsrecapis/MLModels/picklefilesofmodels/tfidf_vectorizer.pkl", 'rb') as f:
        vectorizer = pickle.load(f)
    newsArticles = fetch_news_article()
    newsText = get_newsText(newsArticles)

    vectors = vectorizer.transform(newsText['text'])
    predictions = model.predict(vectors)

    for article, prediction in zip(newsArticles, predictions):
        article['prediction'] = prediction

    return newsArticles

def get_newsWithClass_lr():
    model = None

    with open('newsrecapis/MLModels/picklefilesofmodels/lr_model_cat1.pkl', 'rb') as f:
        model = pickle.load(f)

    vectorizer = None
    with open("newsrecapis/MLModels/picklefilesofmodels/tfidf_vectorizer.pkl", 'rb') as f:
        vectorizer = pickle.load(f)
    newsArticles = fetch_news_article()
    newsText = get_newsText(newsArticles)

    vectors = vectorizer.transform(newsText['text'])
    predictions = model.predict(vectors)

    with open('newsrecapis/MLModels/picklefilesofmodels/label_encoder.pkl', 'rb') as file:
        loaded_le = pickle.load(file)

    decoded_labels = loaded_le.inverse_transform(predictions)

    for article, prediction in zip(newsArticles, decoded_labels):
        article['prediction'] = prediction
        #loaded_le.inverse_transform([prediction])[0] #loaded_le.inverse_transform(prediction)

    return newsArticles

def get_newsWithClass_svm():
    model = None

    with open('newsrecapis/MLModels/picklefilesofmodels/svm_model_cat1.pkl', 'rb') as f:
        model = pickle.load(f)

    vectorizer = None
    with open("newsrecapis/MLModels/picklefilesofmodels/tfidf_vectorizer.pkl", 'rb') as f:
        vectorizer = pickle.load(f)
    newsArticles = fetch_news_article()
    newsText = get_newsText(newsArticles)

    vectors = vectorizer.transform(newsText['text'])
    predictions = model.predict(vectors)

    for article, prediction in zip(newsArticles, predictions):
        article['prediction'] = prediction

    return newsArticles

def get_newsWithClass_svc():
    model = None

    with open('newsrecapis/MLModels/picklefilesofmodels/svc_model_combinedcat.pkl', 'rb') as f:
        model = pickle.load(f)

    vectorizer = None
    with open("newsrecapis/MLModels/picklefilesofmodels/tfidf_vectorizer.pkl", 'rb') as f:
        vectorizer = pickle.load(f)
    newsArticles = fetch_news_article()
    newsText = get_newsText(newsArticles)

    vectors = vectorizer.transform(newsText['text'])
    predictions = model.predict(vectors)

    for article, prediction in zip(newsArticles, predictions):
        article['prediction'] = prediction

    print(newsArticles)
    return newsArticles
