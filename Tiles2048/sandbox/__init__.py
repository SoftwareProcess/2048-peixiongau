import hashlib
import random
from pip._vendor.six import int2byte
from typing import Iterable
hasher = hashlib.sha256(b'test')
##hasher.update(b"test")

test = [1,2,3,4,5,6]
test.append(7)
for a in test:
     
    print(a)


