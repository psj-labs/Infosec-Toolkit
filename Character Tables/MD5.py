md5_map = {
  
    "0cc175b9c0f1b6a831c399e269772661": "a",
    "7fc56270e7a70fa81a5935b72eacbe29": "A",

    "92eb5ffee6ae2fec3ad71c777531578f": "b",
    "9d5ed678fe57bcca610140957afab571": "B",

    "4a8a08f09d37b73795649038408b5f33": "c",
    "0d61f8370cad1d412f80b84d143e1257": "C",

    "e1671797c52e15f763380b45e841ec32": "e",
    "3a3ea00cfc35332cedf6e5e9a32e94da": "E",

    "8fa14cdd754f91cc6554c9e71929cce7": "f",
    "800618943025315f869e4e1f09471012": "F",

    "b2f5ff47436671b6e533d8dc3614845d": "g",
    "dfcf28d0734569a6a693bc8194de62bf": "G",

    "2510c39011c5be704182423e3a695e91": "h",
    "c1d9f50f86825a1a2302ec2449c17196": "H",

    "865c0c0b4ab0e063e5caa3387c1a8741": "i",
    "dd7536794b63bf90eccfd37f9b147d7f": "I",

    "363b122c528f54df4a0446b6bab05515": "j",
    "ff44570aca8241914870afbc310cdb85": "J",

    "8ce4b16b22b58894aa86c421e8759df3": "k",
    "a5f3c6a11b03839d46af9fb43c97c188": "K",

    "2db95e8e1a9267b7a1188556b2013b33": "l",
    "d20caec3b48a1eef164cb4ca81ba2587": "L",

    "6f8f57715090da2632453988d9a1501b": "m",
    "69691c7bdcc3ce6d5d8a1361f22d04ac": "M",

    "7b8b965ad4bca0e41ab51de7b31363a1": "n",
    "8d9c307cb7f3c4a32822a51922d1ceaa": "N",

    "d95679752134a2d9eb61dbd7b91c4bcc": "o",
    "f186217753c37b9b9f958d906208506e": "O",

    "83878c91171338902e0fe0fb97a8c47a": "p",
    "44c29edb103a2872f519ad0c9a0fdaaa": "P",

    "7694f4a66316e53c8cdd9d9954bd611d": "q",
    "f09564c9ca56850d4cd6b3319e541aee": "Q",

    "4b43b0aee35624cd95b910189b3dc231": "r",
    "4b43b0aee35624cd95b910189b3dc231": "R",

    "03c7c0ace395d80182db07ae2c30f034": "s",
    "5dbc98dcc983a70728bd082d1a47546e": "S",

    "e358efa489f58062f10dd7316b65649e": "t",
    "b9ece18c950afbfa6b0fdbfa4ff731d3": "T",

    "7b774effe4a349c6dd82ad4f4f21d34c": "u",
    "4c614360da93c0a041b22e537de151eb": "U",

    "9e3669d19b675bd57058fd4664205d2a": "v",
    "5206560a306a2e085a437fd258eb57ce": "V",

    "f1290186a5d0b1ceab27f4e77c0c5d68": "w",
    "61e9c06ea9a85a5088a499df6458d276": "W",

    "9dd4e461268c8034f5c8564e155c67a6": "x",
    "02129bb861061d1a052c592e2dc6b383": "X",

    "415290769594460e2e485922904f345d": "y",
    "57cec4137b614c87cb4e24a3d003a3e0": "Y",

    "fbade9e36a3f36d3d676c1b808451dd7": "z",
    "21c2e59531c8710156d34a3c30ac81d5": "Z",
}




def find_md5_chars(long_string, md5_map):
    results = []

    for i in range(len(long_string) - 31):
        chunk = long_string[i:i+32]
        if chunk in md5_map:
            results.append((i, chunk, md5_map[chunk]))

    return results



test_data = "input here"

matches = find_md5_chars(test_data, md5_map)

for pos, h, c in matches:
    print(f"loc {pos} → {h} = '{c}'")

# You can look up each character one by one.
