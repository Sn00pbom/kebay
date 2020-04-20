import os
import json
from importlib.machinery import SourceFileLoader


def load_modules():
    modules_path = './modules'
    folder_names = os.listdir(modules_path)
    modules = {}
    manifests = {}
    for f_name in folder_names:
        js_path = os.path.join(modules_path, f_name, 'manifest.json')
        with open(js_path, 'r') as f:
            manifest = json.loads(f.read())
        mod_name = manifest['name']
        mod_path = os.path.join(modules_path, f_name, 'launch.py')
        modules[mod_name] = SourceFileLoader(mod_name, mod_path).load_module()
        manifests[mod_name] = manifest

    return modules, manifests
