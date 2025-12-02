def hex_decode_message(text, count):
    decoded_text = text

    while count > 0:
        decoded_text = bytes.fromhex(decoded_text).decode("utf-8")
        count -= 1

    return decoded_text


encoded = "target"

print(hex_decode_message(encoded, 10))   # 10 times HEX decoding
