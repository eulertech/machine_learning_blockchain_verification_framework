import logging
import os
from blockchain import build_model_chain
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


def build_golden_chain(list_files_golden):
    try:
        chain = build_model_chain(list_files_golden)
    except:
        status = 1
    status = 0
    return status, chain

def build_current_chain(list_files):
    try:
        chain = build_model_chain(list_files)
    except:
        status = 1
    status = 0
    return status, chain

if __name__ == "__main__":

    list_files = ['../Config/config.ini', '../data/raw/raw_data.npy', '../model/model_object/LR.pickle']
    list_files_golden = ['../Config/config.ini', '../data/raw/golden/raw_data.npy', '../model/model_object/golden/LR.pickle']
    logger.info("==================golden chain build======================")
    golden_chain = build_model_chain(list_files_golden)
    logger.info("The length of golden chain is %d"%golden_chain.get_block_length())
    logger.info("==================current chain build======================")
    current_chain = build_model_chain(list_files)
    logger.info("The length of current chain is %d"%current_chain.get_block_length())
    golden_chain.save('../output/golden_chain.txt')
    current_chain.save('../output/current_chain.txt')
    logger.info("Length of golden chain is: %d"%golden_chain.get_block_length())
    golden_chain.print()
    logger.info("Length of current chain is: %d"%current_chain.get_block_length())
