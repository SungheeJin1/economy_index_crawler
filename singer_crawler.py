import time
import selenium
from selenium import webdriver

list = input(print("가수 이름 5개를 입력하시오(콤마로 구분할 것):"))
singerlist=list.split(",") #그래프 그릴 때 x축에 활용

URL = 'https://www.genie.co.kr/'
driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get(url=URL)

for singer in singerlist:
    searchwindow=driver.find_element_by_class_name("ipt-search placeholder")
    searchwindow.send_keys(singer)

    magbtn=driver.find_element_by_class_name("btn-submit")
    magbtn.click()

    songs = driver.find_element_by_class_name("article").text
    print(singer,songs)

    time.sleep(3)
    searchwindow = driver.find_element_by_class_name("ipt-search placeholder")
    searchwindow.clear()

time.sleep(3)

driver.close()