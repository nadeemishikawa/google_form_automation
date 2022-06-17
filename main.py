
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def start_chrome():
    driver = webdriver.Chrome()

    url = "https://docs.google.com/forms/d/e/1FAIpQLSdELat41CE3MvmKScNKONyMSTMtRmGyQQJnOvZ49Y0ApIJ_yQ/viewform"
    driver.get(url)

    return driver

def login_google(driver):
    #ログイン情報
    login_id = "c0b20180ea@edu.teu.ac.jp"

    #最大待機時間（秒）
    wait_time = 30

    ### IDを入力
    login_id_xpath = '//*[@id="identifierNext"]'
    # xpathの要素が見つかるまで待機します。
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, login_id_xpath)))
    driver.find_element_by_name("identifier").send_keys(login_id)
    driver.find_element_by_xpath(login_id_xpath).click()
    time.sleep(3)
    return driver

def password_google(driver):
    # パスワード情報
    login_pw = "6dytuR#9W"

    #最大待機時間（秒）
    wait_time = 30

    ### パスワードを入力
    login_pw_xpath = '//*[@id="passwordNext"]'
    # xpathの要素が見つかるまで待機します。
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, login_pw_xpath)))
    driver.find_element_by_name("password").send_keys(login_pw)
    time.sleep(1) # クリックされずに処理が終わるのを防ぐために追加。
    driver.find_element_by_xpath(login_pw_xpath).click()
    time.sleep(10)
    driver.quit()

if __name__ == "__main__":
    # Chrome起動
    driver = start_chrome()

    # Googleにログイン
    driver = login_google(driver)

    password_google(driver)

import urllib
import  random
def generate_url(url):
    group_name = urllib.parse.quote("セッシー")
    student_number = urllib.parse.quote("C0B20000")
    student_name = urllib.parse.quote("山田太郎")
    place_name = urllib.parse.quote("バイト")


    # 36度1分〜7分になる
    morining_temp = 36 + random.randint(1, 7) / 10
    night_temp = 36 + random.randint(1, 7) / 10

    parameter = "?usp=pp_url&entry.987697424={}&entry.1451746778={}&entry.15528679={}&entry.559706162={}&entry.1257304114={}&entry.793511166={}&entry".format(
        group_name,
        student_number,
        student_name,
        morining_temp,
        night_temp,
        place_name
      )
    new_url = f'{url}?usp=pp_url&entry.987697424={group_name}&entry.1451746778={student_number}&entry.15528679={student_name}&entry.559706162={morining_temp}&entry.60078259={night_temp}&entry.793511166={place_name}&entry'
        # "https://docs.google.com/forms/d/e/1FAIpQLSc0QOFKz0DnOO9Wx9LPX3rs3mNghKRIftLC6SNgalsTJyAF7g/viewform{}".format(parameter)
    return new_url

url = 'https://docs.google.com/forms/d/e/1FAIpQLSdELat41CE3MvmKScNKONyMSTMtRmGyQQJnOvZ49Y0ApIJ_yQ/viewform'
new_page = generate_url(url)
print(new_page)

