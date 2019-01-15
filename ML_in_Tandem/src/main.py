import logging
from build_active_model_chain import build_golden_chain
from build_active_model_chain import build_current_chain
from verify_model_chain import verify_chain
from config import CONFIG

logfile = CONFIG.get('Paths','log_file')
logger = logging.getLogger(__name__)
logging.basicConfig(
    filename=logfile,
    filemode='w',
    format='%(asctime)s %(message)s',
    datefmt='%m%d%Y %I:%M:%S',
    level=logging.DEBUG
)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
logger.addHandler(ch)

logger.info("main program started.")

import config_init
import data_generation  # test data is fixed. No randomness
import data_cleaning
import model_generation
# after model generation, create a block chain
list_files = ['../Config/config.ini', '../data/raw/raw_data.npy', '../model/model_object/LR.pickle']
list_files_golden = ['../Config/config.ini', '../data/raw/golden/raw_data.npy', '../model/model_object/golden/LR.pickle']
rc_create_gold_chain, gold_chain = build_golden_chain(list_files_golden)
rc_create_current_chain, current_chain = build_current_chain(list_files)
gold_chain.save('../output/golden_chain.txt')
current_chain.save('../output/current_chain.txt')
rc_verify_chain = verify_chain(gold_chain, current_chain)
if rc_verify_chain != 0:
    raise AssertionError("The model pipeline does not match")
else:
    import production # start production
logger.info("main program finished.")
