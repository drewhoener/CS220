import re

num = "2.1 dog 3.554 2.8cat"

matches = re.match("\s?(-?[0-9]+)?(\.[0-9]+)?\s", num)
if matches:
    for tup in matches.groups():
        print(tup)
