
import keyboard
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://covid19.kdca.go.kr/'
driver.get(url)

time.sleep(1)
driver.set_window_position(0, 0)
driver.set_window_size(1920, 1080)

time.sleep(1)
WebDriverWait(driver, 6).until(ec.presence_of_element_located(
    (By.CSS_SELECTOR, '#base')))
driver.switch_to.frame('base')

time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR,
                    '#xwup_cert_table > table > tbody > tr > td > div[title="056서경서001"]').click()

time.sleep(0.5)
driver.find_element(By.XPATH,
                    '//*[@id="xwup_certselect_tek_input1"]').send_keys('rudtj5606!')

time.sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="xwup_OkButton"]').click()

time.sleep(0.5)
WebDriverWait(driver, 6).until(ec.presence_of_element_located(
    (By.CSS_SELECTOR, '#base')))
driver.switch_to.frame('base')

time.sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="mCSB_1_container"]/ul/li[6]/a').click()

time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR,
                    '#mCSB_1_container > ul > li.DB_1D.DB_select > ul > li > a').click()

time.sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="header"]/div/button').click()

time.sleep(0.5)
WebDriverWait(driver, 6).until(ec.presence_of_element_located(
    (By.CSS_SELECTOR, 'body')))
driver.switch_to.frame('ifrm')

time.sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="insttSubId"]/option[3]').click()

time.sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="btnSearch"]').click()


def mywait():
    keyboard.read_key()


def my_function5():
    try:
        time.sleep(0.5)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(0.5)
        WebDriverWait(driver, 6).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '#base')))
        driver.switch_to.frame('base')
        driver.switch_to.frame('ifrm')
    except:
        return


def my_function():
    try:
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="inspmet2"]').click()
    except:
        return

    try:
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="btnSave"]').click()
    except:
        return

    try:
        time.sleep(0.5)
        WebDriverWait(driver, 6).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '#modal_confirm.c-modal.c-modal--alert.c-modal--sizeM.has-button.is-active')))
        driver.find_element(By.XPATH,
                            '//*[@id="modal_confirm"]/div[1]/div[2]/button[1]').click()
    except:
        return

    try:
        time.sleep(0.5)
        WebDriverWait(driver, 6).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '#modal_alert.c-modal.c-modal--alert.c-modal--sizeM.has-button.is-active')))
        driver.find_element(By.XPATH,
                            '//*[@id="modal_alert"]/div[1]/div[2]/button').click()
    except:
        return

    try:
        time.sleep(0.5)
        WebDriverWait(driver, 6).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '#sc-print-label.c-modal.has-button.c-modal--sizeP3.is-active')))
        driver.find_element(By.XPATH,
                            '//*[@id="sc-print-label"]/div[1]/div[2]/button[1]').click()
    except:
        return

    try:
        time.sleep(0.5)
        time.sleep(0.5)
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.TAG_NAME,
                            'print-preview-app').shadow_root.find_element(By.ID, 'sidebar').shadow_root.find_element(By.TAG_NAME, 'print-preview-button-strip').shadow_root.find_element(
            By.CSS_SELECTOR, 'div > cr-button.action-button').click()
    except:
        return

    try:
        time.sleep(0.5)
        driver.switch_to.window(driver.window_handles[0])
    except:
        return

    try:
        time.sleep(0.5)
        WebDriverWait(driver, 6).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '#base')))
        driver.switch_to.frame('base')
        driver.switch_to.frame('ifrm')
    except:
        return

    try:
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="btnList"]').click()
    except:
        return


def my_function2():
    try:
        time.sleep(0.5)
        WebDriverWait(driver, 6).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '#modal_confirm.c-modal.c-modal--alert.c-modal--sizeM.has-button')))
    except:
        return

    try:
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="btnSearch"]').click()
    except:
        return


def my_function3():
    try:
        time.sleep(0.5)
        driver.find_element(
            By.CSS_SELECTOR,  '''#btnUpdateOptions''').click()
    except:
        return

    try:
        time.sleep(0.5)
        WebDriverWait(driver, 6).until(
            ec.presence_of_element_located((By.LINK_TEXT, '검사기관 지정')))
    except:
        return

    try:
        time.sleep(0.5)
        driver.find_element(By.LINK_TEXT, '검사기관 지정').click()
    except:
        return

    try:
        time.sleep(0.5)
        WebDriverWait(driver, 6).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '#modal_confirm.c-modal.c-modal--alert.c-modal--sizeM.has-button.is-active')))
    except:
        return

    try:
        time.sleep(0.5)
        driver.find_element(By.CSS_SELECTOR,
                            '#inspctInsttCd [value="210720092626123"]').click()
    except:
        return

    try:
        time.sleep(0.5)
        WebDriverWait(driver, 6).until(ec.presence_of_element_located(
            (By.XPATH, '//*[@id="modal_confirm"]/div[1]/div[2]/button[1]')))
    except:
        return

    try:
        time.sleep(0.5)
        driver.find_element(
            By.XPATH, '//*[@id="modal_confirm"]/div[1]/div[2]/button[1]').click()
    except:
        return

    try:
        time.sleep(0.5)
        WebDriverWait(driver, 6).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '#modal_alert.c-modal.c-modal--alert.c-modal--sizeM.has-button.is-active')))
    except:
        return

    try:
        time.sleep(0.5)
        driver.find_element(
            By.XPATH, '//*[@id="modal_alert"]/div[1]/div[2]/button').click()
    except:
        return

    try:
        time.sleep(0.5)
        WebDriverWait(driver, 6).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '#modal_confirm.c-modal.c-modal--alert.c-modal--sizeM.has-button')))
    except:
        return

    try:
        time.sleep(0.5)
        driver.find_element(
            By.XPATH, '//*[@id="mCSB_2_container"]/div/div[2]/div[1]/div[2]/button[2]').click()
    except:
        return

    try:
        time.sleep(0.5)
        WebDriverWait(driver, 6).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '#modal_confirm.c-modal.c-modal--alert.c-modal--sizeM.has-button.is-active')))
    except:
        return

    try:
        time.sleep(0.5)
        driver.find_element(
            By.XPATH, '//*[@id="modal_confirm"]/div[1]/div[2]/button[1]').click()
    except:
        return

    try:
        time.sleep(0.5)
        WebDriverWait(driver, 6).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '#modal_alert.c-modal.c-modal--alert.c-modal--sizeM.has-button.is-active')))
    except:
        return

    try:
        time.sleep(0.5)
        driver.find_element(
            By.XPATH, '//*[@id="modal_alert"]/div[1]/div[2]/button').click()
    except:
        return


def my_function6():
    try:
        time.sleep(0.8)
        driver.find_element(
            By.CSS_SELECTOR,  '''#btnUpdateOptions''').click()
    except:
        return

    try:
        time.sleep(0.8)
        WebDriverWait(driver, 6).until(
            ec.presence_of_element_located((By.LINK_TEXT, '검사기관 지정')))
    except:
        return

    try:
        time.sleep(0.8)
        driver.find_element(By.LINK_TEXT, '검사기관 지정').click()
    except:
        return

    try:
        time.sleep(0.8)
        WebDriverWait(driver, 6).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '#modal_confirm.c-modal.c-modal--alert.c-modal--sizeM.has-button.is-active')))
    except:
        return

    try:
        time.sleep(0.8)
        driver.find_element(By.CSS_SELECTOR,
                            '#inspctInsttCd [value="210720092626123"]').click()
    except:
        return

    try:
        time.sleep(0.8)
        WebDriverWait(driver, 6).until(ec.presence_of_element_located(
            (By.XPATH, '//*[@id="modal_confirm"]/div[1]/div[2]/button[1]')))
    except:
        return

    try:
        time.sleep(0.8)
        driver.find_element(
            By.XPATH, '//*[@id="modal_confirm"]/div[1]/div[2]/button[1]').click()
    except:
        return

    try:
        time.sleep(0.8)
        WebDriverWait(driver, 6).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '#modal_alert.c-modal.c-modal--alert.c-modal--sizeM.has-button.is-active')))
    except:
        return

    try:
        time.sleep(0.8)
        driver.find_element(
            By.XPATH, '//*[@id="modal_alert"]/div[1]/div[2]/button').click()
    except:
        return

    try:
        time.sleep(0.8)
        WebDriverWait(driver, 6).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '#modal_confirm.c-modal.c-modal--alert.c-modal--sizeM.has-button')))
    except:
        return

    try:
        time.sleep(0.8)
        driver.find_element(
            By.XPATH, '//*[@id="mCSB_2_container"]/div/div[2]/div[1]/div[2]/button[2]').click()
    except:
        return

    try:
        time.sleep(0.8)
        WebDriverWait(driver, 6).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '#modal_confirm.c-modal.c-modal--alert.c-modal--sizeM.has-button.is-active')))
    except:
        return

    try:
        time.sleep(0.8)
        driver.find_element(
            By.XPATH, '//*[@id="modal_confirm"]/div[1]/div[2]/button[1]').click()
    except:
        return

    try:
        time.sleep(0.8)
        WebDriverWait(driver, 6).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '#modal_alert.c-modal.c-modal--alert.c-modal--sizeM.has-button.is-active')))
    except:
        return

    try:
        time.sleep(0.8)
        driver.find_element(
            By.XPATH, '//*[@id="modal_alert"]/div[1]/div[2]/button').click()
    except:
        return


def my_function4():
    try:
        time.sleep(0.5)
        WebDriverWait(driver, 6).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '#modal_confirm.c-modal.c-modal--alert.c-modal--sizeM.has-button')))
    except:
        return

    try:
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="btnPrintOptions"]').click()
    except:
        return

    try:
        time.sleep(0.5)
        WebDriverWait(driver, 6).until(
            ec.presence_of_element_located((By.LINK_TEXT, '튜브용 라벨출력')))
    except:
        return

    try:
        time.sleep(0.5)
        driver.find_element(
            By.XPATH, '//*[@id="uiToggle-1"]/ul/li[2]/a').click()
    except:
        return

    try:
        time.sleep(0.5)
        WebDriverWait(driver, 6).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '#sc-print-label.c-modal.has-button.c-modal--sizeP3.is-active')))
    except:
        return

    try:
        time.sleep(0.5)
        driver.find_element(
            By.XPATH, '//*[@id="sc-print-label"]/div[1]/div[2]/button[1]').click()
    except:
        return

    try:
        time.sleep(0.5)
        time.sleep(0.5)
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.TAG_NAME,
                            'print-preview-app').shadow_root.find_element(By.ID, 'sidebar').shadow_root.find_element(By.TAG_NAME, 'print-preview-button-strip').shadow_root.find_element(
            By.CSS_SELECTOR, 'div > cr-button.action-button').click()
        driver.switch_to.window(driver.window_handles[0])
    except:
        return

    try:
        time.sleep(0.5)
        WebDriverWait(driver, 6).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '#base')))
        driver.switch_to.frame('base')
        driver.switch_to.frame('ifrm')
    except:
        return


def my_function7():
    try:
        time.sleep(0.8)
        WebDriverWait(driver, 6).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '#modal_confirm.c-modal.c-modal--alert.c-modal--sizeM.has-button')))
    except:
        return

    try:
        time.sleep(0.8)
        driver.find_element(By.XPATH, '//*[@id="btnPrintOptions"]').click()
    except:
        return

    try:
        time.sleep(0.8)
        WebDriverWait(driver, 6).until(
            ec.presence_of_element_located((By.LINK_TEXT, '튜브용 라벨출력')))
    except:
        return

    try:
        time.sleep(0.8)
        driver.find_element(
            By.XPATH, '//*[@id="uiToggle-1"]/ul/li[2]/a').click()
    except:
        return

    try:
        time.sleep(0.8)
        WebDriverWait(driver, 6).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '#sc-print-label.c-modal.has-button.c-modal--sizeP3.is-active')))
    except:
        return

    try:
        time.sleep(0.8)
        driver.find_element(
            By.XPATH, '//*[@id="sc-print-label"]/div[1]/div[2]/button[1]').click()
    except:
        return

    try:
        time.sleep(0.8)
        time.sleep(0.8)
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.TAG_NAME,
                            'print-preview-app').shadow_root.find_element(By.ID, 'sidebar').shadow_root.find_element(By.TAG_NAME, 'print-preview-button-strip').shadow_root.find_element(
            By.CSS_SELECTOR, 'div > cr-button.action-button').click()
        driver.switch_to.window(driver.window_handles[0])
    except:
        return

    try:
        time.sleep(0.8)
        WebDriverWait(driver, 6).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '#base')))
        driver.switch_to.frame('base')
        driver.switch_to.frame('ifrm')
    except:
        return


def my_function8():
    try:
        time.sleep(0.5)
        driver.find_element(
            By.XPATH, '//*[@id="grid_dataList_check_all"]').click()
    except:
        return

    try:
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="btnReport"]').click()
    except:
        return

    try:
        time.sleep(0.5)
        WebDriverWait(driver, 6).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '#modal_confirm.c-modal.c-modal--alert.c-modal--sizeM.has-button.is-active')))
    except:
        return

    try:
        time.sleep(0.5)
        driver.find_element(
            By.XPATH, '//*[@id="modal_confirm"]/div[1]/div[2]/button[1]').click()
    except:
        return

    try:
        time.sleep(0.5)
        WebDriverWait(driver, 6).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '#modal_alert.c-modal.c-modal--alert.c-modal--sizeM.has-button.is-active')))
    except:
        return

    try:
        time.sleep(0.5)
        driver.find_element(
            By.XPATH, '//*[@id="modal_alert"]/div[1]/div[2]/button').click()
    except:
        return


keyboard.add_hotkey("f10", my_function)
keyboard.add_hotkey("esc", my_function2)
keyboard.add_hotkey("f8", my_function3)
keyboard.add_hotkey("f9", my_function4)
keyboard.add_hotkey("[", my_function6)
keyboard.add_hotkey("]", my_function7)
keyboard.add_hotkey("p", my_function5)
keyboard.add_hotkey("ctrl+space", my_function8)


while True:
    mywait()
