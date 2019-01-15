import pandas as pd
import numpy as np
import logging
from config import CONFIG
import pickle

logfile = CONFIG.get('Paths','log_file')
logger = logging.getLogger(__name__)
logging.basicConfig(
    filemode='w',
    format='%(asctime)s %(message)s',
    datefmt='%m%d%Y %I:%M:%S',
    level=logging.DEBUG
)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
logger.addHandler(ch)

logger.info("Production module.")

m = CONFIG.get('data_generation','num_samples')
n = CONFIG.get('data_generation', 'num_features')

# load the model and metric
model_save_path = CONFIG['production']['model_object']

with open(model_save_path, 'rb') as f:
    model = pickle.load(f)
logger.info("model saved at: %s"%model_save_path)
logger.info(model)

raw_data_file = CONFIG.get('Paths','raw_data_path') + '/raw_data.csv'
test_data_file = CONFIG.get('Paths','test_data_path') + '/test_data.csv'
logger.info("raw data file is %s\n, test_data_file is: %s" % (raw_data_file, test_data_file))

# load test data
logger.info("load the test data from %s."%test_data_file)
test_data = np.loadtxt(test_data_file,delimiter=',')
#clearning
n_clean = CONFIG.get('data_cleaning','reduced_col_num')
test_data_path = CONFIG.get('Paths','test_data_path') + '/test_data.npy'
data_test_loaded = np.loadtxt(test_data_path,delimiter=',')
X = data_test_loaded[:,0:int(n)]
y = data_test_loaded[:,-1].reshape((X.shape[0],1))
# data cleaning config
dropFeat = CONFIG.getboolean('data_cleaning','drop_feature')
#dropFeat = CONFIG['data_cleaning']['drop_feature']
new_feature_num = CONFIG['data_cleaning']['reduced_col_num']
if dropFeat:
    X_dropped = X[:,0:int(new_feature_num)]
#prediction
y_hat = model.predict(X_dropped)
logger.info("Predicted value is: %s"%str(y_hat))
logger.info("True value is: %s"%str(y))
logger.info("Production is finished. Last step.")
