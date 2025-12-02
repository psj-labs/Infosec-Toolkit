from base64 import b64decode

def decode_message(text, count):
    decoded_text = text

    while count > 0:
        decoded_text = b64decode(decoded_text.encode('utf-8')).decode('utf-8')
        count -= 1

    return decoded_text


encoded = "admin"

print(decode_message(encoded, 20))   # 20 times decoding
