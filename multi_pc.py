from multi_postcode_model import MultiPCModel
from config_manager import *
import requests
import json
import pprint as pp


class MultiPC:
    def __init__(self, postcode_dict):
        self.body = json.dumps(postcode_dict)
        self.headers = {'Content-Type': 'application/json'}
        self.postcode_req = requests.post(base_url(),
                                         headers = self.headers,
                                         data = self.body)
        if self.postcode_req.status_code == 200:
            self.header_details = self.postcode_req.headers
            self.response_json = self.postcode_req.json()
        else:
            print("Error")
            raise

    def get_data(self):
        try:
            return MultiPCModel(self.response_json)
        except:
            print("h")
            raise


trial = MultiPC({"postcodes": ["OX49 5NU", "M32 0JG"]}).get_data()
pp.pprint(trial)
# pp.pprint(trial.response_json['result'][0]['result']['postcode'])


