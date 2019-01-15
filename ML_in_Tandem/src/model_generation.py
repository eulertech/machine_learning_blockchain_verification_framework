import pandas as pd
import numpy as np
import os
import logging
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from config import CONFIG
import pickle

logfile = CONFIG.get('Paths','log_file')
logger = logging.getLogger(__name__)
logging.basicConfig(
#    filename=logfile,
    filemode='w',
    format='%(asctime)s %(message)s',
    datefmt='%m%d%Y %I:%M:%S',
    level=logging.DEBUG
)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
logger.addHandler(ch)

logger.info("model generation module.")

processed_data_path = CONFIG.get('Paths','processed_data_path') + '/processed_data.csv'

try:
    data_processed_loaded = np.loadtxt(processed_data_path, delimiter=',')
except IOError:
    print("Processed data path %s does not exist!"%processed_data_path)
# train the model

X_use = data_processed_loaded[:, 0:2]
y_use = data_processed_loaded[:, -1]
print(X_use.shape, y_use.shape)
reg = LinearRegression().fit(X_use, y_use)

y_pred = reg.predict(X_use)
# save the model and metric
model_save_path = CONFIG['production']['model_object']
metric_save_path = CONFIG['production']['model_features']

score = dict()
score['mse'] = mean_squared_error(y_use, y_pred)

with open(model_save_path, 'wb') as f:
    pickle.dump(reg, f)

with open(metric_save_path, 'wb') as f:
    pickle.dump(score, f)

logger.info("model generation is done.")
