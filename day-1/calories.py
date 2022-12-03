# We need to find the Elf which carries the most calories. 

#file = open("/home/lalvarez/dev/advent-of-code/day-1/test_ds.log")
file = open("/home/lalvarez/dev/advent-of-code/day-1/real_ds.log")

inventories = file.read()
inventories = inventories.split("\n\n")

list_of_inventories = []

for i in inventories:

    temp = i.split("\n")
    for k in temp:
        if k == '':
            temp.remove(k)

    sums = sum([int(val) for val in temp])
    list_of_inventories.append(sums)

print("Number of the Elf with the most calories in his backpack:")
print(list_of_inventories.index(max(list_of_inventories))+1)
print("Number of calories in said backpack:")
print(max(list_of_inventories))

biggest_calories = sum(sorted(list_of_inventories, reverse=True)[:3])

print("Sum of the calories shared by the 3 Elfs carrying the most calories:")
print(biggest_calories)
