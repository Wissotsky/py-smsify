from dataclasses import dataclass, field
from math import ceil
from anyascii import anyascii

basic_table = ("@£$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞ\x1bÆæßÉ !\"#¤%&'()*+,-./0123456789:;<=>?"
       "¡ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÑÜ`¿abcdefghijklmnopqrstuvwxyzäöñüà")
extended_table = ("````````````````````^```````````````````{}`````\\````````````[~]`"
       "|````````````````````````````````````€``````````````````````````")

@dataclass
class SmsMessage:
    """
    Sms Message Representation

    Values:
        Unicode body(body: str) Mandatory!
        Use twilio segmentation(twilio: bool) default=False
        GSM-7 encoded body(encoded_text: str)
        GSM-7 encoded bytes(encoded_bytes: bytes)
        Message length(length: int)
        Message segments(segments: int)
    
    Functions:
        encode(string: str) -> str
        message_encode(plaintext: str) -> bytearray
    """
    body: str
    twilio: bool = False
    encoded_text: str = field(init=False)
    encoded_bytes: bytearray = field(init=False)
    length: int = field(init=False)
    segments: int = field(init=False)
    def __post_init__(self):
        self.encoded_text = SmsMessage.message_encode(self.body).decode()
        self.encoded_bytes = bytes(SmsMessage.message_encode(self.body))
        self.length = len(self.encoded_bytes)
        self.segments = ceil(self.length/(153 if self.twilio and self.length>160 else 160))
    
    def message_encode(plaintext: str) -> bytearray:
        """Encode a unicode string to a bytearray of SMS characters"""
        literatedtext = anyascii(plaintext)
        charbytes = bytearray()
        for character in literatedtext:
            character_index = basic_table.find(character);
            if character_index != -1:
                charbytes.append(character_index)
                continue
            character_index = extended_table.find(character)
            if character_index != -1:
                charbytes.append(27) #escape to extended table
                charbytes.append(character_index)
        return charbytes

    def encode(string: str) -> str:
        """Encode python string into a GSM-7 python encoded string"""
        return SmsMessage.message_encode(string).decode()