import os

def change_dir(path):
    os.chdir(path)

def list_dir():
    return os.listdir()

def make_dir(name):
    os.mkdir(name)

def pwd():
    return os.getcwd()
