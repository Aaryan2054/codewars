
from collections import Counter
k = 0
text = input('Enter any text:')
counter = Counter(text.lower())
for x in counter.values():
    if x>1:
        k=k+1

print (k)
