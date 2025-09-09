import base64
from logs.logger import Logger

logger = Logger.get_logger()


class BdsClassification:
    def __init__(self, text):
        try:
            self.text = text
            self.unkind_words = self.decoding("R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT")
            self.less_iniquitous_words = self.decoding("RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ==")
            logger.info("BdsClassification successfully initialized")
        except Exception as e:
            logger.error(f"error in BdsClassification initialized. error name: {e}")

    def decoding(self, encrypted_text):
        encrypted_text = encrypted_text.encode('ascii')
        decoded_bytes = base64.b64decode(encrypted_text)
        decoded_string = decoded_bytes.decode('utf-8')
        return decoded_string.lower().split(",")

a = BdsClassification("a")
print(type(a.unkind_words) , "\n", a.unkind_words)
print(type(a.less_iniquitous_words) , "\n", a.less_iniquitous_words)