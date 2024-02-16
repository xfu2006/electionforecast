# -----
# Created 01/11/2024
# -----
from itfc import *;
from dummy import *;
from CawDataReader import *;

print("Version 1.2");
#model = MLData(["Date", "Supporters"], [ ["1/1/2024", 20], ["1/2/2024", 30] ], [0.8], [1]);
retriever = DummyRetriever();
data = retriever.retrieve_data("01/01/2024", "01/10/2024");
ml = DummyMLFramework();
model = ml.train(data);
pred = ml.predict(model, model);
print("Dummy prediction is: " + str(pred));

# TEST CODE FOR CawDataReader
caw_reader = CawDataReader("data/small_data/kawintiranon_small_samples.csv");
caw_reader.get_raw_data("09/01/2016", "11/01/2016");



