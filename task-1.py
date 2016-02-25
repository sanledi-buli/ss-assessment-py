import sys
import pdb

"""
Result for sys.getsizeof(arr_ages) is 80MB. I think its safe to use this mechanism.

"""

arr_ages = []
with open('files/ages-10-million.txt') as f:
    for line in f:
        arr_ages.append(int(line.replace('\n','')))

sorted_age = open("files/ages-10-million-shorted.txt","w")

for age in sorted(arr_ages):
    sorted_age.write(str(age) + '\n')
sorted_age.close()