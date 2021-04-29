import hashlib
import random
from pip._vendor.six import int2byte
from typing import Iterable
hasher = hashlib.sha256(b'test')
##hasher.update(b"test")

test = '2'
test += '56'
test = test[:-1]
print(test)


