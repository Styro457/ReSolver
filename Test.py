from SeleniumReCaptcha.ReCaptchaSolver import ImageUtils
from SeleniumReCaptcha.ai.ObjectRecognition import ObjectRecognitionAI
from SeleniumReCaptcha.utils import ImageUtils

objectRecognition = ObjectRecognitionAI()

print(objectRecognition.get_objects(ImageUtils.url_to_image("https://i.imgur.com/D9W7qkR.png")))
