import hashlib
import random
from pip._vendor.six import int2byte
hasher = hashlib.sha256(b'test')
##hasher.update(b"test")

a = '1'
print(bytes(a, 'utf-8'))


