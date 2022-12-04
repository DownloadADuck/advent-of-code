
import numpy as np

file = open("real_ds.log")
rucksacks = file.read()
rucksacks = rucksacks.split("\n")

common_objects = []
total = 0 

for single_sack in rucksacks:
    if single_sack == '':
        print("Break")
        break

    compartment1 = single_sack[:len(single_sack)//2]
    compartment2 = single_sack[len(single_sack)//2:]
    common_objects.extend(set(compartment1).intersection(compartment2))

for obj in common_objects:
    if obj.isupper():
        total += ord(obj) - 38
    else:
        total += ord(obj) - 96
        
print("Sum of priorities:")
print(total)
