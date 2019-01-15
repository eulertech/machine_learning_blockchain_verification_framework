import pandas as pd
import numpy as np
import logging
from config import CONFIG

logfile = CONFIG.get('Paths','log_file')
logger = logging.getLogger(__name__)
logging.basicConfig(
#    filename=logfile,  # this will put all logging to main log file
    filemode='w',
    format='%(asctime)s %(message)s',
    datefmt='%m%d%Y %I:%M:%S',
    level=logging.DEBUG
)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
logger.addHandler(ch)

logger.info("data cleaning module.")

m = CONFIG.get('data_generation','num_samples')
n = CONFIG.get('data_generation', 'num_features')
raw_data_path = CONFIG.get('Paths','raw_data_path') + '/raw_data.csv'
data_raw_loaded = np.loadtxt(raw_data_path, delimiter=',')
X = data_raw_loaded[:,0:int(n)]
y = data_raw_loaded[:,-1].reshape((int(m),1))
# data cleaning config
dropFeat = CONFIG.getboolean('data_cleaning','drop_feature')
#dropFeat = CONFIG['data_cleaning']['drop_feature']
new_feature_num = CONFIG['data_cleaning']['reduced_col_num']
logger.info(type(dropFeat))
if dropFeat:
    processed_data_path = CONFIG.get('Paths','processed_data_path') + '/processed_data.csv'
    logger.info("Drop features")
    X_dropped = X[:,0:int(new_feature_num)]
    data_processed = np.hstack((X_dropped, y))
    np.savetxt(processed_data_path, data_processed, delimiter=',', fmt='%f')

logger.info("Data cleaning is done.")
