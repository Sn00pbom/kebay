import os
import json
from importlib.machinery import SourceFileLoader


def load_modules():
    modules_path = './modules'
    names = os.listdir(modules_path)
    modules = {}
    for name in names:
        path = os.path.join(modules_path, name, 'launch.py')
        modules[name] = SourceFileLoader(name, path).load_module()

    return modules
