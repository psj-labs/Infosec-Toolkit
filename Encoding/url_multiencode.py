from urllib.parse import quote

def url_encode_message(text, count):
    encoded_text = text

    while count > 0:
        encoded_text = quote(encoded_text)
        count -= 1

    return encoded_text


message = "admin' OR 1=1 --"

print(url_encode_message(message, 10))   # 10 times URL encoding
