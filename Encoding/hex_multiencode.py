def hex_encode_message(text, count):
    encoded_text = text

    while count > 0:
        encoded_text = encoded_text.encode("utf-8").hex()
        count -= 1

    return encoded_text


message = "target"

print(hex_encode_message(message, 10))   # 10 times HEX encoding
