import sys
import pdb

arr_ages = []
with open('files/ages-10-million.txt') as f:
    for line in f:
        elems = line.split(',')
        elem = int(elems[0].replace('\n',""))
        arr_ages.append(elem)

sorted_age = open("files/ages-10-million-shorted.txt","w")

for age in sorted(arr_ages):
    sorted_age.write(str(age) + '\n')
sorted_age.close()