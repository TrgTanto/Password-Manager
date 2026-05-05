import os
import sys

def get_data_path(filename):
    base_path = os.path.join(os.getenv("APPDATA"), "PWManager")

    if not os.path.exists(base_path):
        os.makedirs(base_path)

    return os.path.join(base_path, filename)