from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from SeleniumReCaptcha.ai.ObjectRecognition import ObjectRecognitionAI
from SeleniumReCaptcha.ai.SpeechRecognition import SpeechRecognitionAI
from SeleniumReCaptcha.ReCaptchaManager import CaptchaManager
from SeleniumReCaptcha.utils import ImageUtils, TimeUtils

from time import sleep


#ReCaptcha objects to yolo objects
objects = {'bicycles': ['bicycle'],
           'a fire hydrant' : ['fire hydrant'],
           'fire hydrants': ['fire hydrant'],
           'traffic lights': ['traffic light'],
           'crosswalks': ['skip'],
           'stairs': ['skip'],
           'parking meters': ['parking meter'],
           'cars': ['cars', 'truck', 'bus'],
           'bus': ['bus', 'truck']}

class CaptchaSolver:

    def __init__(self, selenium_driver,
                 accesKey="ZO5VAO4EXHYIKVSJA5BBFA5BJJM4SIR3"):

        self.driver = selenium_driver
        self.speechRecognition = SpeechRecognitionAI(accesKey)
        self.objectRecognition = ObjectRecognitionAI()
        self.captchaManager = CaptchaManager(selenium_driver)


    def __solve_captcha_on_page_audio(self):
        self.captchaManager.click_audio()
        TimeUtils.wait_between(0.3, 0.6)
        audio = self.captchaManager.get_audio()
        print("AUDIO: " + audio)

    def __solve_captcha_on_page_image(self):
        global objects
        no_valid_images = False
        while not no_valid_images:
            # What objects you need to click
            needed_objects = objects[self.captchaManager.get_object_type()]

            if 'skip' in needed_objects:
                self.captchaManager.click_refresh()
            else:
                images = self.captchaManager.get_images()
                no_valid_images = True
                tile = 0
                for image in images:
                    objects_in_image = self.objectRecognition.get_objects(image)
                    print(str(objects_in_image))
                    for needed_object in needed_objects:
                        if needed_object in objects_in_image:
                            try:
                                self.captchaManager.click_image(tile)
                                print("CLICKED")
                                no_valid_images = False
                            except:
                                print("NULL")
                    tile += 1
                    TimeUtils.wait_between(0.1, 0.6)
            TimeUtils.wait_between(4, 5)
        self.captchaManager.click_submit()

    def solve_captcha_on_page(self, mode="image"):
        self.captchaManager.click_captcha()
        sleep(0.5)
        if mode == "audio":
            self.__solve_captcha_on_page_audio()
        else:
            self.__solve_captcha_on_page_image()
