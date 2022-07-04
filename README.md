![](https://i.imgur.com/xuHAE49.png)
# Python library for creating GSM-7 compatible SMS messages

### Installation
`pip install py-smsify`

### Usage
```python
from py_smsify import SmsMessage

#Encode to a string of valid characters
message = SmsMessage("Gamer420").encoded_text
# result: Gamer420

#Encode to a python bytestring
message = SmsMessage("Gamer420").encoded_bytes
# result: b"Gamer420"

#Encode with non latin languages
message = SmsMessage("גיימר420").encoded_text
# result: gyymr420

#Encode with emojis
message = SmsMessage("this 🎉 is 👏 phenomenal 🔥").encoded_text
# result: "this :tada: is :clap: phenomenal :fire:"
```