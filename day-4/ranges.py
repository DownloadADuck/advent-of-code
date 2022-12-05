file = open("real.log")
pairs = file.read()
pairs = pairs.split("\n")

count = 0

for line in pairs:
    if line == '':
        break

    x,y = line.split(',')

    x_start, x_end = x.split('-')
    y_start, y_end = y.split('-')

    if (x_start >= y_start and x_end <= y_end):
        count += 1
    elif (y_start >= x_start and y_end <= x_end):
        count += 1

print(count)
