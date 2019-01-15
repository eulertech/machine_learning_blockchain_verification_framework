'''
Script to read config.ini under ../Config folder, and return the object.
'''
import configparser
import os
from configparser import ExtendedInterpolation

DEFAULT_CONFIG_FILE = '../Config/config.ini'


def get_config_file():
    return os.environ.get('CONFIG_FILE', DEFAULT_CONFIG_FILE)


CONFIG_FILE = get_config_file()


def create_config(config_file=None):
    parser = configparser.ConfigParser(interpolation=ExtendedInterpolation())
    parser.read(config_file)
    return parser


CONFIG = create_config(CONFIG_FILE)



