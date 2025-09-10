import base64
from logs.logger import Logger
import string

logger = Logger.get_logger()


class BdsClassification:
    def __init__(self, config):
        try:
            self.cfg = config
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
        try:
            score_text = 0


            text = text.lower()
            translator = str.maketrans('', '', string.punctuation)
            text_without_special_chars = text.translate(translator)
            list_text = [word for word in text_without_special_chars.split() if word]

            for i, word in enumerate(list_text):
                if i + 1 < len(list_text):
                    pair = f"{word} {list_text[i + 1]}"
                    if pair in self.unkind_words:
                        score_text += self.score_unkind_words
                    elif pair in self.less_iniquitous_words:
                        score_text += self.score_less_iniquitous_words

                if word in self.unkind_words:
                    score_text += self.score_unkind_words
                elif word in self.less_iniquitous_words:
                    score_text += self.score_less_iniquitous_words

            bdf_percent = self.get_bdf_percent(len(list_text), score_text)
            bds_thread_level = self.get_bds_thread_level(bdf_percent)
            is_bds = True if bds_thread_level == "high" else False

            dict_of_all_processing = {
                "len text": len(list_text),
                "bds score": score_text,
                "bdf percent": bdf_percent,
                "bds thread level": bds_thread_level,
                "is bds": is_bds
            }

            logger.info("BdsClassification successfully text_processing")
            return dict_of_all_processing
        except Exception as e:
            logger.error(f"error in BdsClassification text_processing. error name: {e}")




    def get_bdf_percent(self, len_text, score_text):
        return round(score_text / len_text * 100, 2)


    def get_bds_thread_level(self, bdf_percent):
        if bdf_percent < self.cfg.SMALE:
            return "none"
        elif self.cfg.SMALE < bdf_percent < self.cfg.MEDIUM:
            return "medium"
        else:
            return "high"
