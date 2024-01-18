# -----
# Created 01/11/2024
# -----
from itfc import *;
from dummy import *;

print("Version 1.2");
#model = MLData(["Date", "Supporters"], [ ["1/1/2024", 20], ["1/2/2024", 30] ], [0.8], [1]);
retriever = DummyRetriever();
data = retriever.retrieve_data("01/01/2024", "01/10/2024");
ml = DummyMLFramework();
model = ml.train(data);
pred = ml.predict(model, model);
print("Dummy prediction is: " + str(pred));


# TODO LIST
# 1. manually define a dummy class (expanding it) the list of
# features and some "real sense" input data several dozens of rows

# 2. real model: search for multi-column timeseries forecast in
# sci-learn

# 3. group research twitter API (I blieve the streaming API is free)
# implementing the DataRetriever child class.:w


