
def change_shuru(driver,url,xp):
    input = driver.find_element_by_xpath(url)
    input.click()
    input.send_keys(xp)