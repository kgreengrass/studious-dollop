from single_pc import SinglePC
from config_manager import *
import requests
import json
import pprint as pp


class MultiPC2(SinglePC):
    def __init__(self, postcodes):
        for x in postcodes:
            self.postcode_req = requests.get(f'{base_url()}{x}')
            if self.postcode_req.status_code == 200:
                self.header_details = self.postcode_req.headers
                self.response_json =  self.postcode_req.json()
            else:
                print("Oh dear, this postcode doesn't exist")



trial = MultiPC2(['LE18 3RW', 'LE18 2HZ', "OX4 5NU"]).get_data()
print(trial.admin_ward)
