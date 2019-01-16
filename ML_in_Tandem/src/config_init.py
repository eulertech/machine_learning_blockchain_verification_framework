'''
This is the configuration part for all the config.
Three sections:
1. data generation , a.k.a data pull
2. model generation configs
3. production configs
'''


import configparser
import datetime
from configparser import ExtendedInterpolation

currentDT = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
#logfilename = 'main_' + str(currentDT) + '.log'
logfilename = 'main_log' + '.log'
config = configparser.ConfigParser(interpolation=ExtendedInterpolation())

config['DEFAULT'] = {'author': r'liang kuang',
                     'date': str(datetime.datetime.now())
}

# config['Paths'] = {'raw_data_path': r'../data/raw/golden',
#                      'processed_data_path': r'../data/processed/golden',
#                      'test_data_path': r'../data/test/golden',
#                      'model_path': r'../model/model_object/golden',
#                      'metric_path': r'../model/metrics/golden',
#                      'output_path': r'../production/output/golden',
#                      'log_file': r'../logs/golden/main.log'}
config['Paths'] = {'raw_data_path': r'../data/raw',
                  'processed_data_path': r'../data/processed',
                  'test_data_path': r'../data/test/golden',
                  'model_path': r'../model/model_object',
                  'metric_path': r'../model/metrics',
                  'output_path': r'../production/output',
                  'log_file': r'../logs/main.log'}

config['data_generation'] = {}
config['data_generation']['num_samples'] = '1000'
config['data_generation']['num_features'] = '4'
config['data_generation']['version_number'] = '1.0'

config['data_cleaning'] = {}
config['data_cleaning']['reduced_col_num'] = '2'
config['data_cleaning']['drop_feature'] = 'True'

config['model_generation'] = {}
config['model_generation']['fit_intercept'] = 'True'
config['model_generation']['metrics'] = 'mse'

config['production'] = {}
config['production']['model_object'] = '${Paths:model_path}/LR.pickle'
config['production']['model_features'] = '${Paths:model_path}/features.csv'
config['production']['output_path'] = '{Paths:output_path}/output'

with open('../Config/config.ini', 'w') as configfile:
    config.write(configfile)


