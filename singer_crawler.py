import time
import selenium
from selenium import webdriver

print("가수 이름 5개를 입력하시오(콤마로 구분할 것)")
print('ex : 아이유,성시경,오마이걸,SG워너비,박재정')
singeranswer=input(">> : ")
singerlist=singeranswer.split(",") #그래프 그릴 때 x축에 활용

URL = 'https://www.genie.co.kr/search/searchMain?query=%25EA%25B0%2580%25EC%2588%2598'
driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get(url=URL)

songnum = []
likes = []

for singer in singerlist:
    searchwindow = driver.find_element_by_xpath("""//*[@id="sc-fd"]""")
    searchwindow.clear()

    searchwindow = driver.find_element_by_xpath("""//*[@id="sc-fd"]""")
    searchwindow.send_keys(singer)

    magbtn=driver.find_element_by_class_name("btn-submit")
    magbtn.click()

    songs = driver.find_element_by_xpath("""//*[@id="body-content"]/div[4]/div[1]/span/strong""").text
    # print(singer,songs)
    songnum.append(songs)

    like = driver.find_element_by_xpath("""/html/body/div[3]/div[2]/div/div[1]/div[3]/div/div[2]/span/a[3]/em""").text
    # print(like)
    likes.append(like)

    time.sleep(2)
    searchwindow = driver.find_element_by_xpath("""//*[@id="sc-fd"]""")
    searchwindow.clear()

time.sleep(2)

driver.close()

print(singerlist)
print(songnum)
print(likes)