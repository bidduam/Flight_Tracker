import enum
import csv

from doctest import OutputChecker
from multiprocessing.sharedctypes import Value
from pydoc import classname
from re import X
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

id = 'yDmH0d'

options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=options, executable_path=r"C:\Users\chris\Downloads\chromedriver_win32\chromedriver.exe")
driver.get(r"https://www.google.com/travel/explore?tfs=CBwQAxoaagwIAhIIL20vMDJjbDESCjIwMjItMDQtMTUaGhIKMjAyMi0wNC0xOXIMCAISCC9tLzAyY2wxcAKCAQsI____________AUABSAGYAQGyAQQYASAB&tfu=GiwaKAoSCTGwzB_9KE5AEUdDRWpYb0hAEhIJSBnode8mQkAR4_LqVp5AKMAgAw")
wait = WebDriverWait(driver,10)
titles = wait.until(EC.text_to_be_present_in_element((By.ID, 'yDmH0d'),'About'))

#Scrape Chrome for element text for each city in XPATHs_List list.
elementtext = (driver.find_element(by=By.ID, value =id).text).replace("\n", "> ").split('> ')[20:]
slicepoint = elementtext.index('About')
destlist = elementtext[:slicepoint]

#Variables
city            = destlist[0::5]
dates           = destlist[1::5]
stops           = destlist[2::5]
flighttime      = destlist[3::5]
price           = destlist[4::5]    

keynum = range(len(destlist[0::5]))

#City Dictionary
citydict = {}

for key, value in enumerate(city):
    citydict[value] = dates[key], stops[key], flighttime[key], price[key]

#Dictionary Search Function
def get_citykey(val):
    for key, value in citydict.items():
        if val == value:
            return key

    return "Unable to find key for ", val

#Output Results
for i in keynum:
    print("City: " , city[i])
    print("\nDates: ", dates[i])
    print("\nStops: ", stops[i])
    print("\nFlight Time: ", flighttime[i])
    print("\nPrice: ", price[i])
