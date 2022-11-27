# rc-image-tile-33
import undetected_chromedriver as uc

from SeleniumReCaptcha.ReCaptchaSolver import CaptchaSolver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from random import uniform

from time import sleep

options = uc.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("user-agent=Chrome/88.0.3729.169")
options.add_argument('--disable-extensions')
options.add_argument('--profile-directory=Default')
options.add_argument('--disable-blink-features=AutomationControlled')
driver = uc.Chrome(options=options)


def wait_between(a, b):
    rand = uniform(a, b)
    sleep(rand)


captchaSolver = CaptchaSolver(driver)
driver.get("https://patrickhlauke.github.io/recaptcha/")

sleep(2)

captchaSolver.solve_captcha_on_page()


"""wait_between(0.8, 1.2)
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
wait_between(0.1, 0.5)
driver.switch_to.default_content()
wait_between(0.5, 0.9)
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='c-'][src^='https://www.google.com/recaptcha/api2/bframe?']")))
wait_between(0.1, 0.3)
images = driver.find_elements_by_class_name("rc-image-tile-wrapper")
#try:
for image in images:
    img = image.find_element_by_class_name("rc-image-tile-33")
    print(img.tag_name)
    print(img.get_attribute("src"));
    image = img.get_attribute("src");
    break;
#except:
#    print("NOT 33")
try:
    for image in images:
        img = image.find_element_by_class_name("rc-image-tile-44")
        print(img.tag_name)
        #print(img.getAttribute("src"));
except:
    print("NOT 44")
input("CLOSE")"""
