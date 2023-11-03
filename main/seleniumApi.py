import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class SeleniumApi:
    __tmpPath = 'main/tmp'

    def get_screenshot(self, url: str, filename: str):
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--start-maximized')
        options.add_argument('--headless=new')
        result = False

        options.add_extension('main/crx/IIFCHHFNNMPDBIBIFMLJNFJHPIFIFFOG_1_2_13_0.crx')
        #options.add_extension('main/crx/CJPALHDLNBPAFIAMEJDNHCPHJBKEIAGM_1_52_2_0.crx')

        driver = webdriver.Chrome(options=options)
        try:
            driver.get(url)
            time.sleep(2)

            elem = driver.find_element(By.TAG_NAME, 'body')
            height = driver.execute_script("return document.body.scrollHeight")
            driver.set_window_size(1920, height)

            print(height)

            result = driver.save_screenshot(f"{self.__tmpPath}/{filename}")
        except Exception:
            print(Exception)
            pass
        finally:
            driver.close()
            driver.quit()

        print(result)
        return result

    def execute_console_command(self, url: str, command: str):
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--headless=new')
        options.add_argument('--start-maximized')
        result = False

        #options = webdriver.ChromeOptions()
        options.add_extension('main/crx/IIFCHHFNNMPDBIBIFMLJNFJHPIFIFFOG_1_2_13_0.crx')
        #options.add_extension('main/crx/CJPALHDLNBPAFIAMEJDNHCPHJBKEIAGM_1_52_2_0.crx')

        driver = webdriver.Chrome(options=options)
        try:
            driver.get(url)
            time.sleep(1)

            #command = ''
            #result = driver.execute_script('return Math.ceil(0.6)')
            #result = driver.execute_script("return 'mozilla'.length")
            result = driver.execute_script(f"return {command}")
            #time.sleep(2)
        except Exception:
            print('$$$$$')
            print(Exception)
            pass
        finally:
            driver.close()
            driver.quit()
        print('!!!!!')
        print(result)
        return result
