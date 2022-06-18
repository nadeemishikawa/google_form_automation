from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import urllib
import random

GROUP_NAME = 'セッシー'
STUDENT_NUMBER = 'C0B20000'
STUDENT_NAME = 'やｍだ'
LOGIN_ID = 'メールアドレス'
PASSWORD = 'パスワード'


def generate_url(url):
    # パラメータに入力する値をURLエンコード
    group_name = urllib.parse.quote(GROUP_NAME)
    student_number = urllib.parse.quote(STUDENT_NUMBER)
    student_name = urllib.parse.quote(STUDENT_NAME)
    place_name = urllib.parse.quote("バイト")
    check_box01 = urllib.parse.quote("ありません。")
    check_box02 = urllib.parse.quote("了解しました。")

    # 36度〜36度7分になる
    morining_temp = 36 + random.randint(1, 7) / 10
    night_temp = 36 + random.randint(1, 7) / 10

    # 事前入力されたurlを生成
    new_url = f'{url}?usp=pp_url&entry.987697424={group_name}&entry.1451746778={student_number}&entry.15528679={student_name}&entry.559706162={morining_temp}&entry.60078259={night_temp}&entry.793511166={place_name}&entry.963226943={check_box01}&entry.52692009={check_box02}'
    return new_url


def start_chrome(url):
    driver = webdriver.Chrome()
    driver.get(url)

    return driver


def login_google(driver):
    # ログイン情報
    login_id = LOGIN_ID

    # 最大待機時間（秒）
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
    login_pw = PASSWORD

    # 最大待機時間（秒）
    wait_time = 30

    # パスワードを入力
    login_pw_xpath = '//*[@id="passwordNext"]'
    # xpathの要素が見つかるまで待機します。
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, login_pw_xpath)))
    driver.find_element_by_name("password").send_keys(login_pw)
    time.sleep(3)  # クリックされずに処理が終わるのを防ぐために追加。
    driver.find_element_by_xpath(login_pw_xpath).click()
    time.sleep(5)
    try:
        url = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[2]/a').get_attribute('href')
        driver.get(url)
    except:
        None
    time.sleep(4)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    next_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    next_button.click()

    time.sleep(2)
    next_button = driver.find_elements_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    print(next_button)
    next_button[1].click()
    time.sleep(10)

    driver.quit()


if __name__ == "__main__":
    url = 'https://docs.google.com/forms/d/e/1FAIpQLSdELat41CE3MvmKScNKONyMSTMtRmGyQQJnOvZ49Y0ApIJ_yQ/viewform'
    new_url = generate_url(url)
    # Chrome起動
    driver = start_chrome(new_url)

    # Googleにログイン
    driver = login_google(driver)

    password_google(driver)
