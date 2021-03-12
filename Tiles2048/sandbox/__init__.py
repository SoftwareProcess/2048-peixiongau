import hashlib

hasher = hashlib.sha256(b'test')
##hasher.update(b"test")

test = {"a":1};
print(hasher.digest())

