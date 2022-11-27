import undetected_chromedriver.v2 as uc
from time import sleep
from SeleniumReCaptcha.ReCaptchaSolver import CaptchaSolver

driver = uc.Chrome()

with driver:
    captchaSolver = CaptchaSolver(driver)
    driver.get("https://patrickhlauke.github.io/recaptcha/")
    sleep(1)
    captchaSolver.solve_captcha_on_page(mode='audio')
    while True:
        a = 0