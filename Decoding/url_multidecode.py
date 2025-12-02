from urllib.parse import unquote

def url_decode_message(text, count):
    decoded_text = text

    while count > 0:
        decoded_text = unquote(decoded_text)
        count -= 1

    return decoded_text


encoded = "target"

print(url_decode_message(encoded, 10))   # 10 times URL decoding
