import base64
from logs.logger import Logger
import string

logger = Logger.get_logger()


class BdsClassification:
    def __init__(self):
        try:
            self.unkind_words = self.decoding("R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT")
            self.less_iniquitous_words = self.decoding("RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ==")
            self.score_unkind_words = 2
            self.score_less_iniquitous_words = 1

            logger.info("BdsClassification successfully initialized")
        except Exception as e:
            logger.error(f"error in BdsClassification initialized. error name: {e}")

    def decoding(self, encrypted_text):
        encrypted_text = encrypted_text.encode('ascii')
        decoded_bytes = base64.b64decode(encrypted_text)
        decoded_string = decoded_bytes.decode('utf-8')
        return decoded_string.lower().split(",")

    def text_processing(self, text: str):
        score_text = 0


        text = text.lower()
        translator = str.maketrans('', '', string.punctuation)
        text_without_special_chars = text.translate(translator)

        list_text = text_without_special_chars.split(" ")
        counter = 0
        while counter < len(list_text):
            for word in self.unkind_words:
                if " " in word:
                    if counter + 1 < len(list_text):
                        word_pairs = str(word).split(" ")
                        score_text += self.get_score_from_word_pairs(word_pairs, list_text[counter], list_text[counter + 1], "unkind_words")
                        continue

                else:
                    if list_text[counter] == word:
                        score_text += self.score_unkind_words
                        continue

            for word in self.less_iniquitous_words:
                if " " in word:
                    if counter + 1 < len(list_text):
                        word_pairs = str(word).split(" ")
                        score_text += self.get_score_from_word_pairs(word_pairs, list_text[counter], list_text[counter + 1], "less_iniquitous_words")


                else:
                    if list_text[counter] == word:
                        score_text += self.score_less_iniquitous_words

            counter += 1
        print(score_text)

    def get_score_from_word_pairs(self, word_pairs: list, first_word: str, second_word: str, type_word: str):
        if first_word == word_pairs[0] and second_word == word_pairs[1]:
            if type_word == "unkind_words":
                return self.score_unkind_words
            elif type_word == "less_iniquitous_words":
                return self.score_less_iniquitous_words
        return 0






a = BdsClassification()
print(a.unkind_words)
print(a.less_iniquitous_words)
a.text_processing("genocide war crimes flotilla resistance freedom nakba flotilla freedom")


