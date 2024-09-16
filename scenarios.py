from sel import Driver
from soup import Soup
from dolp import Dolphin

class Scenarios:
    def __init__(self):
        self.dolp = Dolphin()
        self.dolp.run_profile()
        automation_params = self.dolp.automation
        self.sel = Driver(automation_params['port'])

    def __del__(self):
        self.sel.close_driver()
        #self.dolp.stop_profile()
    #1. перейти на страницу
    #2. Retrieve the source page
    #3. Try to find news elements (headers, pictures, texts) according to "instructions"
    #4. If news elements don't found according to default instruction, alert user to create a new one

    def newsLinkScenario(self):
        link_example = 'https://www.db.com/news/detail/20240731-deutsche-bank-launches-basf-s-first-sustainability-linked-payables-finance-program-in-asia?language_id=1'
        
        self.sel.goToPage(link_example)

        with open('link_example', 'w') as f:
            f.write(self.sel.driver.page_source)

        
    # === Instructions


sc = Scenarios()
sc.newsLinkScenario()