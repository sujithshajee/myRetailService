import json
import os


def load_json(path):
    print("[+] Loading json from path: {}".format(path))
    directory_of_this_file = os.path.dirname(os.path.realpath(__file__))
    full_path = os.path.join(directory_of_this_file, "../", path)
    full_path = os.path.realpath(full_path)
    with open(full_path, "r") as f:
        data = f.read()
    return json.loads(data)
