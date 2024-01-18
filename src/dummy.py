# DUMMY implementation
from itfc import *;

class DummyMLModel(MLModel):

	def __init__(self):
		self.num = 1;

	def save_to(fpath):
		print("DUMMY: save model to: " + fpath);

	def load_from(fpath):
		print("DUMMY: load model from: " + fpath);


class DummyMLFramework(MLFramework):

	def __init__(self):
		self.num = 1;

	def train(self, mldata):
		return DummyMLModel();

	def predict(self, ml_model, ml_data):
		return 0.9;

	def backtest(self, ml_model, ml_data):
		return {"accuracy": 0.9};

class DummyRetriever(DataRetriever):
	def __init__(self):
		self.num = 1;

	def retrieve_data(self, start_date, end_date):
		model = MLData(["Date", "Supporters"], [ ["1/1/2024", 20], ["1/2/2024", 30] ], [0.8], [1]);
		return model

