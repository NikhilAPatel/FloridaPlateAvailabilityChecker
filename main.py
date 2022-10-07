from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()


def os():
    o1 = driver.find_element(By.ID, "MainContent_lblOutPutRowOne")
    o2 = driver.find_element(By.ID, "MainContent_lblOutPutRowTwo")
    o3 = driver.find_element(By.ID, "MainContent_lblOutputRowThree")
    o4 = driver.find_element(By.ID, "MainContent_lblOutputRowFour")
    o5 = driver.find_element(By.ID, "MainContent_lblOutputRowFive")
    return [o1, o2, o3, o4, o5]


def ginputs():
    driver.get("https://services.flhsmv.gov/MVCheckPersonalPlate/PlateInquiryView.aspx")
    elem1 = driver.find_element(By.NAME, "ctl00$MainContent$txtInputRowOne")
    elem2 = driver.find_element(By.NAME, "ctl00$MainContent$txtInputRowTwo")
    elem3 = driver.find_element(By.NAME, "ctl00$MainContent$txtInputRowThree")
    elem4 = driver.find_element(By.NAME, "ctl00$MainContent$txtInputRowFour")
    elem5 = driver.find_element(By.NAME, "ctl00$MainContent$txtInputRowFive")
    return [elem1, elem2, elem3, elem4, elem5]


def submit():
    driver.find_element(By.NAME, "ctl00$MainContent$btnSubmit").click()


letters = 'abcdefghijklmnopqrstuvwxyz0123456789'

availables = []

entries = []

for l1 in letters:
    for l2 in letters:
        for l3 in letters:
            entries.append(l1 + l2 + l3)

entrylist = []
inputs = ginputs()
i = 0
for entry in entries:
    inputs[i].send_keys(entry)
    entrylist.append(entry)
    i += 1
    if (i >= 5):
        i = 0
        submit()
        outputs = os()
        for j in range(0, 5):
            if outputs[j].get_attribute('innerHTML') == "AVAILABLE":
                availables.append(entrylist[j])
                print(entrylist[j])
        entrylist = []
        inputs = ginputs()
