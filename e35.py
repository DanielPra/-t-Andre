# Varför blir detta knas?

import json
from collections import Counter

with open("birthdays.json", "r") as f:
    info = json.load(f)

for x in info.values():
    months = x
    print(months)

countmonths = Counter(months)
print(countmonths)

sandwiches = ["ham", "cheese", "roast beef", "ham", "cheese", "roast beef", "ham"]
c = Counter(sandwiches)

"""
26:e februari
10:e juli
6:e oktober
14:e mars
1:a september
18:e juni
7:e augusti
14:e juli
8:e december
17:e juli
Counter({'1': 1, '7': 1, ':': 1, 'e': 1, ' ': 1, 'j': 1, 'u': 1, 'l': 1, 'i': 1})
PS C:\Users\inbad\dantest\lpthw>    """                                                                                                                                                                                                                       
