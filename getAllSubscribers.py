from selenium import webdriver
import time
import loginInfos
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

url = "https://www.instagram.com"

browser.get(url)
browser.maximize_window()
time.sleep(1)

username = browser.find_element(By.NAME, 'username')
password = browser.find_element(By.NAME, 'password')

username.send_keys(loginInfos.userName)
password.send_keys(loginInfos.password)

loginButton = browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]/button")
loginButton.click()

time.sleep(10)

notNow = browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button")
notNow.click()

time.sleep(10)

notification = browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
notification.click()
time.sleep(10)

goToProfile = browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/div/a")
goToProfile.click()

time.sleep(10)

followers = browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a")
followers.click()
time.sleep(10)

jscommand = """
followers = document.querySelector("._aano");
followers.scrollTo(0, followers.scrollHeight);
var lenOfFollowerPage = followers.scrollHeight;
return lenOfFollowerPage;
"""

lenOfFollowerPage = browser.execute_script(jscommand)
followerMatch = False
while (followerMatch == False):
    lastCount = lenOfFollowerPage
    time.sleep(7)
    lenOfFollowerPage = browser.execute_script(jscommand)
    if lastCount == lenOfFollowerPage:
        followerMatch = True

time.sleep(10)

followersList = []
followers = browser.find_elements(By.CSS_SELECTOR,".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.notranslate._a6hd")

for follower in followers:
    followersList.append(follower.text)

quitFollower = browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button")
quitFollower.click()

time.sleep(10)

followings = browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a")
followings.click()

time.sleep(10)

lenOfFollowingPage = browser.execute_script(jscommand)
followingMatch = False
while (followingMatch == False):
    lastCount = lenOfFollowingPage
    time.sleep(7)
    lenOfFollowingPage = browser.execute_script(jscommand)
    if lastCount == lenOfFollowingPage:
        followingMatch = True

followingList = []
followings = browser.find_elements(By.CSS_SELECTOR,".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.notranslate._a6hd")

for following in followings:
    followingList.append(following.text)


netList = []
for item in followingList:
    if(item in followersList):
        pass
    else:
        netList.append(item)


with open("takip etmeyenler.txt","w",encoding="UTF-8") as file:
    for item in netList:
        file.write(item + "\n")

browser.close()