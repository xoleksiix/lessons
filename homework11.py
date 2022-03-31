import string
import random

dict_1 = {keys: values
          for keys in [random.choice(string.ascii_letters[:26])
                       for _ in range(10)]
          for values in [random.randint(0, 9) for _ in range(10)]}
dict_2 = {keys: values
          for keys in [random.choice(string.ascii_letters[:26])
                       for _ in range(10)]
          for values in [random.randint(0, 9) for _ in range(10)]}
dict_total = {}

for i in dict_1.keys():
    if dict_total.get(i) is None:
        dict_total[i] = dict_1[i]
    else:
        if dict_total[i] < dict_1[i]:
            dict_total[i] = dict_1[i]

for i in dict_2.keys():
    if dict_total.get(i) is None:
        dict_total[i] = dict_2[i]
    else:
        if dict_total[i] < dict_2[i]:
            dict_total[i] = dict_2[i]

print(dict_1)
print(dict_2)
print(dict_total)
