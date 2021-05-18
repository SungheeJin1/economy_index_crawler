import time
import selenium
from selenium import webdriver
import matplotlib.pyplot as plt
import numpy as np

print("가수 이름 5개를 입력하시오(콤마로 구분할 것)")
print('ex : 아이유,성시경,오마이걸,SG워너비,박재정')
singeranswer=input(">>")
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

songnum1=[]
for n in songnum:
    new = ''
    for i in n:
        if i.isalnum():
            new+=i
        else:
            continue
    songnum1.append(new)

songnum2=[]
for i in songnum1:
    t=float(i)
    songnum2.append(t)

likes1=[]
for n in likes:
    new = ''
    for i in n:
        if i.isalnum():
            new+=i
        else:
            continue
    likes1.append(new)

likes2=[]
for i in likes1:
    t=float(i)
    likes2.append(t)

time.sleep(2)

driver.close()

print('가수 이름',singerlist)
print('가수 별 곡 건수',songnum2)
print('가수 별 좋아요 수',likes2)

x1 = np.arange(5)
plt.figure(1)
plt.rc('font', family='Malgun Gothic')
plt.suptitle('가수 별 곡 건수')
plt.bar(x1,songnum2)
plt.xticks(x1, singerlist)
plt.show()

x=np.arange(5)
plt.figure(2)
plt.suptitle('가수 별 좋아요 수')
plt.rc('font', family='Malgun Gothic')
plt.bar(x, likes2)
plt.xticks(x, singerlist)
plt.show()