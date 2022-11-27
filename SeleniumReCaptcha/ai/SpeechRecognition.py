from wit import Wit

class SpeechRecognitionAI():
    client = None

    def __init__(self, accessKey):
        client = Wit(accessKey)

    def speech_to_text(self, file, contentType):
        with open(file, 'rb') as f:
            resp = self.client.speech(f, {'Content-Type': contentType})
        return str(resp)