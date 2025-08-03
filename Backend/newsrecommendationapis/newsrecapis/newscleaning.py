import re
import string
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
import nltk
import shutil
import os

# Remove existing punkt data
# punkt_dir = os.path.join(nltk.data.find('tokenizers'), 'punkt')
# if os.path.exists(punkt_dir):
#     shutil.rmtree(punkt_dir)

# # Re-download punkt
# nltk.download('punkt')
# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

# Initialize the default stemmer and stopwords
default_stemmer = PorterStemmer()
default_stopwords = stopwords.words('english') + ['said', 'would', 'even', 'according', 'could', 'year',
                                                  'years', 'also', 'new', 'people', 'old', 'one', 'two',
                                                  'time', 'first', 'last', 'say', 'make', 'best', 'get',
                                                  'three', 'make', 'year old', 'told', 'made', 'like',
                                                  'take', 'many', 'set', 'number', 'month', 'week', 'well',
                                                  'back']

BAD_SYMBOLS_RE = re.compile("[^a-zA-Z,\d]")
REPLACE_IP_ADDRESS = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')

def clean_text(text):
    # Tokenize text
    def tokenize_text(text):
        return [w for s in sent_tokenize(text) for w in word_tokenize(s) if len(w) >= 3]

    # Preprocess text (lowercase, remove special characters, etc.)
    def preprocessing_text(text):
        text = text.lower()
        text = text.replace('\n', ' ').replace('\xa0', ' ').replace('-', ' ')
        text = re.sub(r'\d+', '', text)
        text = re.sub(r'http\S+', '', text)
        text = BAD_SYMBOLS_RE.sub(' ', text)
        text = REPLACE_IP_ADDRESS.sub('', text)
        text = REPLACE_BY_SPACE_RE.sub(' ', text)
        return text

    # Remove stopwords from text
    def remove_stopwords(text, stop_words=default_stopwords):
        tokens = tokenize_text(text)
        return ' '.join([w for w in tokens if w not in stop_words])

    # Lemmatize text
    def lemmatize_text(text, lemm=WordNetLemmatizer()):
        tokens = tokenize_text(text)
        return ' '.join([lemm.lemmatize(t) for t in tokens])

    # Clean the text
    text = preprocessing_text(text)
    text = ' '.join(filter(None, [t for t in tokenize_text(text) if t not in string.punctuation]))
    text = lemmatize_text(text)
    text = remove_stopwords(text)

    return text
