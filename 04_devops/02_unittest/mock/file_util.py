import json
from collections import OrderedDict

from pandas.io.json import json_normalize


def get_data_frame_from_json_file(json_file_path):
    with open(json_file_path) as f:
        json_object = json.loads(f.read(), object_pairs_hook=OrderedDict)
    return json_normalize(json_object)
