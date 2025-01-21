from math import log10
from random import random

for i in range(1, 10):
    print(i, log10((i + 1) / i))

# arr = [log10((i + 1) / i) for i in range(1,10)]

arr = [
    0.3010299956639812,
    0.17609125905568124,
    0.12493873660829993,
    0.09691001300805642,
    0.07918124604762482,
    0.06694678963061322,
    0.05799194697768673,
    0.05115252244738129,
    0.04575749056067514,
]


def benford():
    r = random()

    for i in range(1, 10):
        r -= arr[i - 1]
        if r <= 0:
            return i


res = list()
for _ in range(1000):
    res.append(benford())

for i in range(1, 10):
    print(i, res.count(i))
