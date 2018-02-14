from collections import Counter
from random_number import random_num

#calling random_num function 2000 times
l = []
for i in range(1000):
    l.append(random_num())


# verifying bias by checking the counter
d = Counter(l)
print(d)


greater_numbers = list(filter(lambda x: x >= 5, l))
print(len(greater_numbers)/len(l))