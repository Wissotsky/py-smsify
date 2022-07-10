from py_smsify import SmsMessage
from urllib.request import urlopen

WINNIE_THE_POOH = "https://gist.githubusercontent.com/SkyDiverCool/2ef648623b1b24580637a53fc6d8e1ea/raw/61656ecbfe897b76c5f960c0eb4c1b49a87b8d44/winniethepooh.txt"

def test_text_field():
    assert SmsMessage("Cool Message!").encoded_text == "Cool Message!"

def test_bytes_field():
    assert SmsMessage("Cool Message!").encoded_bytes == b'Cool Message!'

def test_language():
    assert SmsMessage("酷短信！").encoded_text == "KuDuanXin!"

def test_emoji():
    assert SmsMessage("Cool😎 Message✉️").encoded_text == "Cool:sunglasses: Message:envelope:"

def test_message_length():
    assert SmsMessage("He\\o W{}rld!").length == 15
    assert SmsMessage("Cool Message!").length == 13

def test_message_segments():
    assert SmsMessage("Short message with less than one segment").segments == 1

def test_winniethepoohsize():
    text = urlopen(WINNIE_THE_POOH).read().decode()
    assert SmsMessage(text).length == 454
    assert SmsMessage(text).segments == 3
    assert SmsMessage(text,twilio=True).segments == 3