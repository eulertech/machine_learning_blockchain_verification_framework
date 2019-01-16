import numpy as np
import logging
from config import CONFIG

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

logger.info('data generation module.')

logger.info(CONFIG['Paths']['author'])
logger.info(CONFIG.get('Paths','author'))

# data generation config
m = CONFIG.get('data_generation','num_samples')
n = CONFIG.get('data_generation', 'num_features')
X = np.random.random([int(m),int(n)])
y = np.dot(X, np.array(np.arange(1,int(n)+1)),).reshape((int(m),1)) + 3
x_test = np.asarray(int(n)*[22]).reshape((1,int(n)))
y_test = np.asarray(1*[.5]).reshape((1,1))

raw_data_path = CONFIG.get('Paths','raw_data_path') + '/raw_data.csv'
logger.info(raw_data_path)
data_raw = np.hstack((X,y))
#np.save(raw_data_path, data_raw)
np.savetxt(raw_data_path, data_raw, delimiter=',', fmt='%f')

test_data_path = CONFIG.get('Paths','test_data_path') + '/test_data.csv'
logger.info(test_data_path)
data_test = np.hstack((x_test,y_test))
np.savetxt(test_data_path, data_test, delimiter=',', fmt='%f')

logger.info("data generation is done.")
