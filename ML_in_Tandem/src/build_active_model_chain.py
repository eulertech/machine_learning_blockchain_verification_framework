import logging
import os
from blockchain import build_model_chain

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
    golden_chain = build_model_chain(list_files_golden)
    current_chain = build_model_chain(list_files)
    golden_chain.save('../output/golden_chain.txt')
    current_chain.save('../output/current_chain.txt')
    print("Length of golden chain is: %d"%golden_chain.get_block_length())
    golden_chain.print()
    print("Length of current chain is: %d"%current_chain.get_block_length())
