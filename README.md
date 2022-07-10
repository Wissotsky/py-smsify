![](https://i.imgur.com/xuHAE49.png)
# Python library for creating GSM-7 compatible SMS messages

### Installation
`pip install py-smsify`

### Standalone Functions
```python
from py_smsify import SmsMessage

# Encode python string into a GSM-7 python encoded string
SmsMessage.encode(string: str) -> str

# Encode a unicode string to a bytearray of SMS characters
SmsMessage.message_encode(string: str) -> bytearray
```

### Usage
```python
from py_smsify import SmsMessage

#Encode to a string of valid characters
message = SmsMessage("Cool Message!").encoded_text
# result: Cool Message!

#Encode to a python bytestring
message = SmsMessage("Cool Message!").encoded_bytes
# result: b"Cool Message!"

#Encode with non latin languages/characters
message = SmsMessage("酷短信！").encoded_text
# result: KuDuanXin!

#Encode with emojis
message = SmsMessage("Cool😎 Message✉️").encoded_text
# result: "Cool:sunglasses: Message:envelope:"
```

### Message Stats
```python
from py_smsify import SmsMessage

#Get message length in bytes
message = SmsMessage("Cool Message!").length
# result: 13 bytes
message = SmsMessage("He\\o W{}rld!").length #{} are characters from the extended table and therefore require 2 bytes of space
# result: 15 bytes

#Get amount of segments the message will be split to
message = SmsMessage("Cool Message!").segments
# result: 1 message

#You can also have it calculate segment count with twilio message headers in mind
message = SmsMessage("Cool Message!",twilio=True).segments
# result: 1 message

```