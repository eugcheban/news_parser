import os

from typing import Optional
from requests import request
from time import sleep

class Dolphin():
    def __init__(self):
        self.url = "https://dolphin-anty-api.com/browser_profiles"
        self.id = os.environ.get('DOLPHIN_PROFILE_ID', None)
        self.params = {
            'limit': 50,
            'page': 1
        }
        self.headers = {
            'Authorization': os.environ.get('DOLPHIN_API', None)
        }
        self.automation = None

    def get_profiles(self):
        response = request("GET", self.url, headers=self.headers, params=self.params)
        response.raise_for_status()
        print(response.json())

    def run_profile(self):
        url = f'http://localhost:3001/v1.0/browser_profiles/{self.id}/start?automation=1'
        response = request("POST", url)
        response.raise_for_status()

        
        if response.status_code == 200:
            data = response.json()  
            if 'automation' in data:
                print(f'Data automation: {data["automation"]}')
                self.automation = data['automation']
            else:
                raise KeyError("Key 'automation' not found in the response")
        else:
            response.raise_for_status()

    def stop_profile(self):
        url = f'http://localhost:3001/v1.0/browser_profiles/{self.id}/stop'
        response = request("GET", url)
        
        if response.status_code == 200:
            print("Profile successfully closed!")
        else:
            response.raise_for_status()

#get_profiles()
if __name__ == '__main__':
    dl = Dolphin()
    dl.run_profile()
    sleep(10)
    dl.stop_profile()