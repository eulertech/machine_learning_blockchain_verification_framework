import logging
import os
from blockchain import compare_model_chains

def verify_chain(chain1, chain2):
    if compare_model_chains(chain1, chain2):
        status = 0
    else:
        status = 1
    return status

