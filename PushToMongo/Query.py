import pymongo
import pandas as pd
import numpy as np
from keras.models import model_from_json

def model_load(json_path, model_path):
    # Reload model and parameters
    json_file = open(json_path, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    trained_model = model_from_json(loaded_model_json)
    trained_model.load_weights(model_path)
    print("Loaded model from disk")

    return trained_model

uri = 'mongodb://chickenlittle:butter@ds255797.mlab.com:55797/population_db'

client = pymongo.MongoClient(uri)
db = client.get_database('population_db')
data = db['individual_db']
cursor = data.find({}).limit(5)

LOOK_BACK = 5
N_FEATURES = 4

breathing_rate = list()
oxygen_saturation = list()
heart_rate = list()
label = list()
i = 1
for document in cursor:
    label.append(document['label'])
    heart_rate.append(document['heart_rate'])
    oxygen_saturation.append(document['oxygen_saturation'])
    breathing_rate.append(document['breathing_rate'])


# Concat labels into numpy array
currTest = np.vstack((label, heart_rate, oxygen_saturation, breathing_rate))
print(currTest.shape)

# make a prediction
currTest = np.reshape(currTest, (1, LOOK_BACK, N_FEATURES))
model = model_load('model.json', 'model.h5')
yhat = model.predict_classes(currTest)

print(yhat)

client.close