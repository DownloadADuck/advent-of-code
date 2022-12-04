# Day-3 part 2

file = open("test_ds.log")
rucksacks = file.read()
rucksacks = rucksacks.split("\n")

elf_1 = []
elf_2 = []
elf_3 = []

for i in rucksacks[::3]:
    if i == '':
        break
    elf_1.append(i)
for i in rucksacks[1::3]:
    if i == '':
        break
    elf_2.append(i)
for i in rucksacks[2::3]:
    if i == '':
        break
    elf_3.append(i)

first_comparison = []
second_comparison = []

for (elf1, elf2) in zip(elf_1, elf_2):
    first_comparison.append(set(elf1).intersection(elf2)) 

print(first_comparison)
print(elf_3)

for (first_comp, elf3) in zip(first_comparison, elf_3):
    second_comparison.extend(set(first_comp).intersection(elf3))
    #print(second_comparison)
        
#print("Sum of priorities:")
#print(total)

#print([rucksacks[i] for i in (1,2,3)])
