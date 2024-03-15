# NLTK sentimantal analysis
# Author: Xiang Fu
# Date: 03/15/2023
# code adapted from examples in:
# URL1: https://www.datacamp.com/tutorial/text-analytics-beginners-nltk

from itfc import *;
import nltk;
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# create preprocess_text function from:  URL1
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    processed_text = ' '.join(lemmatized_tokens)
    return processed_text

class NTLKSentAnalyzer(AbstractSentimentAnalyzer):
	def sentiment_analyze(self, txt, topic):
		#print("DEBUG USE 102");
		#nltk.download("all");
		txt2 = preprocess_text(txt);
		print("DEBUT USE 103: preprocessed:", txt2);
		analyzer = SentimentIntensityAnalyzer()
		scores = analyzer.polarity_scores(txt2);
		print("DEBUG USE 104: scores: ", scores);
		return scores["pos"];
