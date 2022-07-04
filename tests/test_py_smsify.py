from py_smsify import __version__
from py_smsify import SmsMessage

def test_version():
    assert __version__ == '0.1.0'

def test_object_repr():
    assert repr(SmsMessage("Gamer420")) == "Gamer420"

def test_text_field():
    assert SmsMessage("Gamer420").encoded_text == "Gamer420"

def test_bytes_field():
    assert SmsMessage("Gamer420").encoded_bytes == b'Gamer420'

def test_language():
    assert SmsMessage("גיימר420").encoded_text == "gyymr420"

def test_emoji():
    assert SmsMessage("this 🎉 is 👏 phenomenal 🔥").encoded_text == "this :tada: is :clap: phenomenal :fire:"

def test_message_length():
    assert SmsMessage("Gamer{}420").length == 12

def test_message_segments():
    assert SmsMessage("Gamer420").segments == 1