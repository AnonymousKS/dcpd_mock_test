def logical_main(username, password):
    import time

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait


    driver = webdriver.Chrome()

    driver.get('https://uims.cuchd.in/uims/')

    WebDriverWait(driver, 10)

    def login():
        driver.find_element(By.ID, 'txtUserId').send_keys(username)
        driver.find_element(By.ID, 'btnNext').click()

        WebDriverWait(driver, 30)

        driver.find_element(By.ID, 'txtLoginPassword').send_keys(password)

        time.sleep(10)

        driver.find_element(By.ID, 'btnLogin').click()

        WebDriverWait(driver, 10)

        driver.maximize_window()
        time.sleep(2)

    def select_test():
        # click on DCPD on left pane
        driver.find_element(By.XPATH, '//*[@id="menu-content"]/li[9]/a').click()
        time.sleep(1)

        # click on evening cucat
        driver.find_element(By.XPATH, '//*[@id="3713"]/li[9]/a').click()
        time.sleep(1)

        # click on mock teet
        driver.find_element(By.XPATH, '//*[@id="3714"]/li[1]/a').click()
        time.sleep(3)

    def logical():
        # select logical reasoning
        driver.find_element(By.XPATH, '//*[@id="ddltest"]/option[2]').click()
        time.sleep(1)

        # select submit
        driver.find_element(By.XPATH, '//*[@id="btnSubmit"]').click()
        time.sleep(1)

        # click on read instruction
        driver.find_element(By.XPATH, '//*[@id="chkAgree"]').click()
        time.sleep(1)

        # click on continue
        driver.find_element(By.XPATH, '//*[@id="btnContinue"]').click()
        time.sleep(1)

        # click start test
        driver.find_element(By.XPATH, '//*[@id="btnStart"]').click()
        time.sleep(1)

        # click ok
        driver.find_element(By.XPATH, '/html/body/div[3]/div/div/button[1]').click()
        time.sleep(2)

        # select option
        driver.find_element(By.XPATH, '//*[@id="rbopt1"]').click()
        time.sleep(2)

        for i in range(2, 31):
            # select next question
            driver.find_element(By.XPATH,
                                f'/html/body/form/div[4]/div[2]/div/div[3]/div[8]/div[2]/div/div[4]/div[1]/ol/li[{i}]/div[1]').click()
            time.sleep(2)
            # select option
            driver.find_element(By.XPATH, '//*[@id="rbopt1"]').click()
            time.sleep(2)

        driver.close()

    login()
    select_test()
    logical()
