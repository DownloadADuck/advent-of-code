# Second part of the problem. We are now using the strategy guide as intended.
# We cannot use a case matrix here. Trying other stuff.

enemy_choices = []
match_results = []
result_list = []

with open('real_ds.log') as file:
    for line in file:
        enemy_choices.append(line.split()[0])
        match_results.append(line.split()[1])

def win_lose_value(match_result, value):
    match match_result:
        case 'X':
            match value:
                case 'A':
                    played_value = 3 #'C'
                case 'B':
                    played_value = 1 #'A'
                case 'C':
                    played_value = 2 #'B'
        case 'Y':
            match value:
                case 'A':
                    played_value = 1 + 3 #'A'
                case 'B':
                    played_value = 2 + 3 #'B'
                case 'C':
                    played_value = 3 + 3 #'C'
        case 'Z':
            match value:
                case 'A':
                    played_value = 2 + 6 #'B'
                case 'B':
                    played_value = 3 + 6 #'C'
                case 'C':
                    played_value = 1 + 6 #'A'
    return played_value

for (result, choice) in zip(match_results, enemy_choices):
    result_list.append(win_lose_value(result, choice))

print("Score when following the guide:")
print(sum(result_list))
