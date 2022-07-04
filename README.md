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

### Message Stats
```python
from py_smsify import SmsMessage

#Get message length in bytes
message = SmsMessage("Gamer420").length
# result: 8 bytes
message = SmsMessage("Gamer{}420").length #{} are characters from the extended table and therefore require 2 bytes of space
# result: 12 bytes

#Get amount of segments the message will be split to
message = SmsMessage("Gamer420").segments
# result: 1 message

#You can also have it calculate segment count with twilio message headers in mind
message = SmsMessage("Gamer420",twilio=True).segments
# result: 1 message

```