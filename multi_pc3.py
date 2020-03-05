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
        if self.postcode_req.status_code == 200:
            for x in self.response_json['result']:
                try:
                    return MultiPCModel(x)
                except:
                    print("h")
                    raise
        else:
            print("BOOOOOOOO")


trial = MultiPC({"postcodes": ["OX49 5NU", "M32 0JG", "LE18 3RW"]}).get_data()
print(trial.codes_admin_county)
print(trial.admin_ward)
# # pp.pprint(trial.response_json['result'][0])
# print(len(trial.response_json['result']))
# pp.pprint(trial.response_json['result'][0]['result']['postcode'])


