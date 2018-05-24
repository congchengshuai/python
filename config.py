#coding=utf8
import os

try:
    import ConfigParser as configparser
except:
    import configparser as configparser

__all__ = ['config']

def _init():
    config = configparser.ConfigParser()
    real_path = os.path.dirname(os.path.abspath(__file__))
    config.read(os.path.join(real_path,"conf.conf"))
    return config

config = _init()