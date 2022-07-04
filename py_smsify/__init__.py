__version__ = '0.1.0'

from dataclasses import dataclass, field
from anyascii import anyascii

basic_table = ("@£$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞ\x1bÆæßÉ !\"#¤%&'()*+,-./0123456789:;<=>?"
       "¡ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÑÜ`¿abcdefghijklmnopqrstuvwxyzäöñüà")
extended_table = ("````````````````````^```````````````````{}`````\\````````````[~]`"
       "|````````````````````````````````````€``````````````````````````")

def message_encode(plaintext):
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

@dataclass
class SmsMessage:
    body: str
    encoded_text: str = field(init=False)
    encoded_bytes: bytearray = field(init=False)
    def __post_init__(self):
        self.encoded_text = message_encode(self.body).decode()
        self.encoded_bytes = bytes(message_encode(self.body))
    
    def __repr__(self):
        return self.encoded_text