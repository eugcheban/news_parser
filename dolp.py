from typing import Optional
from requests import request
from time import sleep

class Dolphin():
    def __init__(self):
        self.url = "https://dolphin-anty-api.com/browser_profiles"
        self.id = 441578767
        self.params = {
            'limit': 50,
            'page': 1
        }
        self.headers = {
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiY2U1YmYzNTYwZGYzODM5NGYwNjdjMzY5MGJiZWY0N2ZlNmRlMDU0NWEwY2YyMDBjYzNlOWNmYzNiZjkzYTEyZjVkOGYzODI1YTk1OTI2ZTkiLCJpYXQiOjE3MjQwOTUxMTUuMTI1NzQxLCJuYmYiOjE3MjQwOTUxMTUuMTI1NzQyLCJleHAiOjE3NTU2MzExMTUuMTExNzI1LCJzdWIiOiIzMzMyOTk1Iiwic2NvcGVzIjpbXX0.Yo0idPIEwd7lg9jPK-UK-QMijxe48Qe7sqU4E3kwCnUzoH6YzZrc0A1Oqmy1jRoHNFR2bzPfD-xXsiBiA4hVjBuAO_pufUseljgoNYnXc2b9G2iGi4qLitTy2l8ipLIq6zzsRisbnR7-3Kmufxp8lfiS6ZHc6VJROGVGrIeOt73SyjnWaJepxB0TgeA4MqeqxDODtSk3-i2Lfp7ePELPhnu4lAwg1V7LhM0unJ3Q87HblXxkGcJ03ydxkopvFPUQ7XY0ue7ulVodkw8jzkhTtP6w2jboPvoyCvgbsJOEKxmxXVZ6JbbdDYuZDfPTTgn3B08-aEHiBPBNSbHKY2O9Ctz-6p96Dv-kl5O7b7OhsnwJky3Q-I3BPIzqVkZ0lau7U3eXaoQ32-Ie6YsvSUGGPs1-LZc71Q-xh2JPEELdmhCRZCOBxyeXT43dEa5ZdPgb30fLiSFyoYVZ7t5ZnIPx7VkoCfwe4zofdYx6OepqWvqFSiaZASsuc2JCMsvLE5gVhvDwrQa8rID7QLz8up4LiSOs5EHy8Lh-ck7hFbEI4hOCbWQQQCBWCmGJLi0XEL68H1PZxCdun27BgRsBOTZa50lHYBnnYT9xlW0Com9d2H3aw34qoY88vNn_V8gPmv2NihS1OAyQTrwpZAg5lNI3eK_XBxq-GhKHao6VeWLRmaw',
        }
        self.automation = None

    def get_profiles(self):
        response = request("GET", self.url, headers=self.headers, params=self.params)
        response.raise_for_status()
        print(response.json())

    def run_profile(self, id=441578767):
        url = f'http://localhost:3001/v1.0/browser_profiles/{id}/start?automation=1'
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

    def stop_profile(self, id=441578767):
        url = f'http://localhost:3001/v1.0/browser_profiles/{id}/stop'
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