from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

class pullData:

    def __init__(self, years, base_url, write_location, pages):
        self.years = years
        self.base_url = base_url
        self.write_location = write_location
        self.pages = pages
        self.browser = webdriver.Chrome('/path/to/chromedriver')

    def grabData(self):
        url = ''
        for year in self.years:
            for page in range(1,self.pages):
                if(page == 1):
                    url = self.base_url + year + '/results/#'
                    self.browser.get((url))
                    time.sleep(3)
                    self.writeData(year, page)
                else:
                    url = self.base_url + year + '/results/#/page/' + str(page) + '/'
                    self.browser.get((url))
                    time.sleep(3)
                    self.writeData(year, page)


    def writeData(self, year, page):
        page_name = self.write_location + year + 'page-' + str(page) + '.htm'
        with open(page_name, 'w') as f:
            f.write(self.browser.page_source)

#nba = pullData(['2018-2019', '2017-2018'], "https://www.oddsportal.com/basketball/usa/nba-", "/path/to/sports-booking/data/nba/", 29)
#nba.grabData()
mlb = pullData(['2018'], "https://www.oddsportal.com/baseball/usa/mlb-", "path/to/sports-booking/data/mlb/", 10)
mlb.grabData()
mlb.browser.quit()
