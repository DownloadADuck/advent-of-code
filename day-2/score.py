# What would be my score if everything goes exactly according to the strategy guide? 

import numpy as np

case_mat = np.array([[4, 8, 3], [1, 5, 9], [7, 2, 6]])

case_list=[]
lines=[]
col=[]

with open('real_ds.log') as file:
    for line in file:
        lines.append(line.split()[0])
        col.append(line.split()[1])

def replace_coord(array, A, B, C):
    array[array==A] = 0
    array[array==B] = 1
    array[array==C] = 2
    return array.astype(int)

lines_coord = replace_coord(np.array(lines), 'A', 'B', 'C')
col_coord = replace_coord(np.array(col), 'X', 'Y', 'Z')

for i in range(0, len(lines_coord)):
    case_list.append(case_mat[lines_coord[i], col_coord[i]])

print("The total score is:")
print(sum(case_list))
