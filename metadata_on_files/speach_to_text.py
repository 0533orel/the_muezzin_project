import speech_recognition as sr
from logs.logger import Logger


logger = Logger.get_logger()

class SpeachToText:
    def __init__(self):
        try:
            self.model = sr.Recognizer()
            logger.info("SpeachToText successfully initialized")
        except Exception as e:
            logger.error(f"error in SpeachToText initialized. error name: {e}")

    def transcribe(self, file_path):
        try:
            with sr.AudioFile(file_path) as source:
                audio_data = self.model.record(source)
                text = str(self.model.recognize_google(audio_data))
                logger.info("SpeachToText successfully transcribe")
                return text
        except Exception as e:
            logger.error(f"error in SpeachToText transcribe. error name: {e}")
