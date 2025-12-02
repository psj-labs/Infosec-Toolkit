from base64 import b64encode

def encode_message(text, count):
    encoded_text = text

    while count > 0:
        encoded_text = b64encode(encoded_text.encode('utf-8')).decode('utf-8')
        count = count - 1

    return encoded_text

message = "target"

print(encode_message(message, 20))   # 20 times encoding
