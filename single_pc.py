from config_manager import *
from single_postcode_model import  SinglePCModel
import requests
import json

class SinglePC:
    def __init__(self, postcode):
        #make an api request
        # store header info in self.header_details
        # store the json retrieved in self.repsonse_json
        self.postcode_req = requests.get(f'{base_url()}{postcode}')
        if self.postcode_req.status_code == 200:
            self.header_details = self.postcode_req.headers
            self.response_json =  self.postcode_req.json()
        else:
            print("Oh dear, this postcode doesn't exist")


    def get_data(self):
        #return singlePCModel intialised with the json
        try:
            return SinglePCModel(self.response_json)
        except AttributeError:
            print('Error')


trial = SinglePC('LE18 3RW').get_data()

