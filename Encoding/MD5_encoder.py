import hashlib

def md5_hash(text: str) -> str:
    return hashlib.md5(text.encode()).hexdigest()

if __name__ == "__main__":
    s = "a"
    h = md5_hash(s)
    print("Input:", s) #input
    print("MD5 :", h) #output
