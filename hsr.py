from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chromedriver = '/Users/phoebecho/Desktop/sel/chromedriver'
first_url = 'https://www.thsrc.com.tw/'
url = 'https://irs.thsrc.com.tw/IMINT/?locale=tw&_ga=2.109641158.2111313683.1658301358-1529050216.1658301358'
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

class HSR():

    def __init__(self):
        self.driver = webdriver.Chrome(chromedriver)

        
    def run(self):
        windows = self.go_to_the_website()
        self.click_cookie_1()
        self.select_location01()
        self.select_location02()
        self.select_depart_date()
        self.run_search()
        self.select_train()
        self.press_order()
        self.click_cookie(windows)
        self.round_trip()
        self.select_cabin()
        self.select_seat()
        self.select_search_method()
        self.start_station()
        self.destination_station()
        self.depart_date()
        self.depart_time()
        self.return_date()
        self.return_time()
        self.wait_for_verification_code()
        self.click_submit()


    # To the HSR website
    def go_to_the_website(self):
        self.driver.get(first_url)
        self.driver.maximize_window()  # 要用maximize_window才能把畫面最大化，找到我們要的畫面視窗跟點擊
        windows = self.driver.current_window_handle
        return windows

    # Click accept cookie btn policy
    def click_cookie_1(self):
        cookie = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div[3]/button[2]').click()

    # Select location01
    def select_location01(self):
        location01 = self.driver.find_element(By.ID, 'select_location01')
        Select(location01).select_by_visible_text('南港')
    
    # Select location01
    def select_location02(self):
        location02 = self.driver.find_element(By.ID, 'select_location02')
        Select(location02).select_by_visible_text('左營')
    
    # Select depart date
    def select_depart_date(self):
        d_date01 = self.driver.find_element(By.ID, 'Departdate01')
        d_date01.click()
        d_date01_table = self.driver.find_element(By.CLASS_NAME, 'table-condensed')
        d_date01_table.find_element(By.XPATH, '//*[@id="Departdate01"]').click()

    # Run search
    def run_search(self):
        self.driver.find_element(By.ID, 'start-search').click()

    # select train
    def select_train(self):
        # train = self.driver.find_element(By.ID, 'timeTableTrain_S')
        self.driver.implicitly_wait(5)
        train = self.driver.find_element(By.XPATH, '//*[@id="timeTableTrain_S"]/a[1]')
        train.click()

    #  press order
    def press_order(self):
        order = self.driver.find_element(By.ID, 'order').click()


    # // PAGE 2 // #



    # Click accept cookie btn policy
    def click_cookie(self, windows):
        self.driver.implicitly_wait(5)
        c = self.driver.window_handles
        for w in c:
            if (w != windows):
                self.driver.switch_to.window(w)
        cookie = self.driver.find_element(By.ID, 'cookieAccpetBtn')
        cookie.click()
        return windows

    # Select round trip
    def round_trip(self):
        self.driver.implicitly_wait(10)
        trip = self.driver.find_element(By.ID, 'BookingS1Form_tripCon_typesoftrip')
        Select(trip).select_by_visible_text('去回程')

    # Select cabin
    def select_cabin(self):
        cabin = self.driver.find_element(By.ID, 'BookingS1Form_trainCon_trainRadioGroup')
        Select(cabin).select_by_visible_text('商務車廂')

    # Select seat
    def select_seat(self):
        seat = self.driver.find_element(By.ID, 'BookingS1Form_seatCon_seatRadioGroup')
        Select(seat).select_by_visible_text('靠窗優先')

    # Select search method
    def select_search_method(self):
        select_time = self.driver.find_element(By.XPATH, '//*[@id="BookingS1Form"]/div[2]/div[2]/div/label[1]/input')
        select_time.click()

    # Select starting station
    def start_station(self):
        start = self.driver.find_element(By.XPATH, '//*[@id="BookingS1Form"]/div[3]/div[1]/div/div[1]/div/select')
        Select(start).select_by_visible_text('南港')

    # Select destinating station
    def destination_station(self):
        destination = self.driver.find_element(By.XPATH, '//*[@id="BookingS1Form"]/div[3]/div[1]/div/div[2]/div/select')
        Select(destination).select_by_visible_text('左營')

    # Select depart date
    def depart_date(self):
        d_date = self.driver.find_element(By.XPATH, '//*[@id="BookingS1Form"]/div[3]/div[2]/div/div[1]/div[1]/input[2]')
        d_date.click()
        d_date_table = self.driver.find_element(By.CLASS_NAME, 'flatpickr-day')
        d_date_table.find_element(By.XPATH, '//*[@id="mainBody"]/div[9]/div[2]/div/div[2]/div[1]/span[34]').click()

    # Select depart time
    def depart_time(self):
        d_time = self.driver.find_element(By.XPATH, '//*[@id="BookingS1Form"]/div[3]/div[2]/div/div[2]/div[1]/select')
        Select(d_time).select_by_visible_text('00:00')

    # Select return date
    def return_date(self):
        r_date = self.driver.find_element(By.XPATH, '//*[@id="BookingS1Form"]/div[3]/div[2]/div/div[1]/div[2]/input[2]')
        r_date.click()
        r_date_table = self.driver.find_element(By.CLASS_NAME, 'flatpickr-day')
        r_date_table.find_element(By.XPATH, '//*[@id="mainBody"]/div[10]/div[2]/div/div[2]/div[1]/span[35]').click()

    # Select return time
    def return_time(self):
        r_time = self.driver.find_element(By.XPATH, '//*[@id="BookingS1Form"]/div[3]/div[2]/div/div[2]/div[3]/select')
        Select(r_time).select_by_visible_text('00:00')

    # enter verification code
    def wait_for_verification_code(self):
        input('Press enter when done with verification')

    # submit
    def click_submit(self):
        self.driver.find_element(By.ID, 'SubmitButton').click()


if __name__ == '__main__':
    hsr = HSR()
    hsr.run()


