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
    login_id = "c0b200135b@edu.teu.ac.jp"
    login_pw = "j43e%hjHQ"

    #最大待機時間（秒）
    wait_time = 30

    ### IDを入力
    login_id_xpath = '//*[@id="identifierNext"]'
    # xpathの要素が見つかるまで待機します。
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, login_id_xpath)))
    driver.find_element_by_name("identifier").send_keys(login_id)
    driver.find_element_by_xpath(login_id_xpath).click()

    ### パスワードを入力
    login_pw_xpath = '//*[@id="passwordNext"]'
    # xpathの要素が見つかるまで待機します。
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, login_pw_xpath)))
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys(login_pw)
    time.sleep(1) # クリックされずに処理が終わるのを防ぐために追加。
    driver.find_element_by_xpath(login_pw_xpath).click()
    time.sleep(100)
    driver.quit()

if __name__ == "__main__":
    # Chrome起動
    driver = start_chrome()

    # Googleにログイン
    login_google(driver)