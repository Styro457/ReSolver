from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from SeleniumReCaptcha.utils import ImageUtils


class CaptchaManager:
    def __init__(self, selenium_driver):
        self.driver = selenium_driver

    def solve_captcha(self):
        print("AAAAAA")

    def click_captcha(self):
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
            (By.CSS_SELECTOR, "iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
        self.driver.switch_to.default_content()
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
            (By.CSS_SELECTOR, "iframe[name^='c-'][src^='https://www.google.com/recaptcha/api2/bframe?']")))

    def click_submit(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='recaptcha-verify-button']"))).click()

    def click_image(self, tile):
        self.driver.find_elements_by_class_name("rc-imageselect-tile")[tile].click()

    def click_audio(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='recaptcha-audio-button']"))).click()

    def click_refresh(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='recaptcha-reload-button']"))).click()

    def type_audio_response(self, response):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='audio-response']"))).send_keys(response)

    def get_audio(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//audio[@id='audio-source']"))).get_attribute("src")

    def get_image(self, tile):
        images = self.driver.find_elements_by_class_name("rc-image-tile-wrapper")
        try:
            image = images[tile].find_element_by_class_name("rc-image-tile-33")
            # The image is the full image and needs to be cropped
            if image is not None:
                link = image.get_attribute("src")
                return ImageUtils.cut_image_in_tiles(ImageUtils.url_to_image(link), 3, 3)[tile]
        except NoSuchElementException:
            # The image is just the tile image
            image = images[tile].find_element_by_class_name("rc-image-tile-11")
            if image is not None:
                link = image.get_attribute("src")
                return ImageUtils.url_to_image(link)

    def get_images(self):
        result = []
        for i in range(9):
            image = self.get_image(i)
            if image is not None:
                result.append(image)
        return result

    def get_object_type(self):
        return self.driver.find_element_by_class_name("rc-imageselect-desc-no-canonical").text.split("\n")[1]
