# -----------------------------------
# This class defines all model class
# and the ABSTRACT Interface that are to be
# implemented
# 
# Created: 01/18/2024
# -----------------------------------

from abc import ABC, abstractmethod

# models data source:
#  (1) 2-d main data, each column is a feature (e.g.,
#      #positive_posts, #fav_score, #density_posts
#  (2) verification data (poll results). 1-d vector
#      e.g., frequency (simplify the model
#      IF there are multiple polling agency results, we will
#       aggregate them into one array)
#      * to support join with 2-d main data: include another
#      # vector of indexes with points to the record in 2-d main data
# NOTE: this is a CONCRETE CLASS, not an abstract class
class MLData:
	# constructor (default)
	def __init__(self):
		# column titles
		self.cols = ["Date"];

		# 2d data (each row MUST HAVE same number of columns as cols)
		self.data2d = [ ["01-01-2024"] ];

		# verification data (like poll results)
		self.verif_data = [ [1.0] ];

		# join_index, which links a record in verif_data back to data2d
		self.join_idx = [ 0 ];

	# real constructor for building MLData instance
	def __init__(self, cols, data2d, verif_data, join_idx):
		self.cols = cols;
		self.data2d = data2d;
		self.verif_data = verif_data;
		self.join_idx = join_idx;

	# construct another instance which projects the entire data set
	# to a subset of columns
	def project_cols(self, subset_cols):
		raise Exception("project_cols not implemented yet");

	def save_to(self, fpath):
		raise Exception("save_to not implemented yet");

	def load_from(self, fpath):
		raise Exception("load from not implemented");

	# merge with another model (assuming columns are the same)
	def merge_with(self, other_model):
		raise Exception("merge_with not implemented");
		

# abstract class for the model generated
class MLModel(ABC):
	@abstractmethod
	def save_to(fpath):
		pass;

	@abstractmethod
	def load_from(fpath):
		pass;

# abstract class for ML framework, needs to be implemented	
class MLFramework(ABC):

	# given the training data (instance of MLData)
	# generate the model
	# return an instance of MLModel
	@abstractmethod
	def train(self, mldata):
		pass;

	# given an instance of ml_data (we ONLY takes the 2d main data and cols)
	# return a prediction of a floating point number
	@abstractmethod
	def predict(self, ml_model, ml_data):
		pass;

	# will take advantantage of verif_data
	# returns a dictionary {recall_rate, accuracy_rate} -> TO BE DETERMINED
	@abstractmethod
	def backtest(self, ml_model, ml_data):
		pass;

# abstract class for building up the input data
# e.g., retrieve data from Twitter
# WILL have additional processing POWER
class DataRetriever(ABC):
	# need to return an instance of MLData
	@abstractmethod
	def retrieve_data(self, start_date, end_date):
		pass;

	# from the raw_data returned by the data reader
	# process by DAY (e.g., 1000 tweets in a specific day)
	# extract features
	# e.g., returns data like
	#    date          support_rate    dislike_rate
	# [
	#   ['01/01/2024', 0.9,             0.05     ],
	#   ['01/02/2024', 0.85,            0.05     ],
	# ]
	@abstractmethod
	def build_data(self, raw_data):
		# you should call SentimentalAnalyzer class to
		# rate each tweet, and aggregate the stats data.
		pass;

	# given the data returned by build_data, save to file
	@abstractmethod
	def save_data_to(self, processed_data, filename):
		pass;

	#abstractmethod
	def load_data_from(self, filename):
		pass;

# abstract class for RAW data reader 
# JUST return RAW TEXT of tweets or information without further processing
class RawDataReader(ABC):
	# need to return an ARRAY of the following (array of TUPLES of two elements
	# [(time_stamp, RAW_STRING (e.g., tweet))]
	# e.g. [
	# 		('01/09/2020 12:00:05pm', 'tweet raw string: trump is great'),
	# 		('01/09/2020 12:00:06pm', 'tweet raw string: trump is great'),
	#		]
	@abstractmethod
	def get_raw_data(self, start_date, end_date):
		return [];


# analyzer of sentimental analysis
class AbstractSentimentAnalyzer(ABC):
	# return a score between 0.0 (hate) to 1.0 (support), 0.5 for neutral
	@abstractmethod
	def sentiment_analyze(self, txt, topic):
		return 0.5;











