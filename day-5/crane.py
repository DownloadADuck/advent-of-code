# We are trying to move each crate pile following the dirrections.
# We need to have the final crates that sit on top of each pile.

import sys

def move(piles, from_pile, to_pile, n):
    for i in range(n):
        piles[to_pile].append(piles[from_pile].pop())

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 {} <input_file>".format(sys.argv[0]))
        sys.exit(1)

    strip_file(sys.argv[1])


    with open(sys.argv[1]) as f:
        lines = f.readlines()
    
    print(lines)
    piles = [[] for i in range(4)]
    for line in lines:
        if line.startswith("move"):
            n, from_pile, to_pile = [int(x) for x in line.split()[1:]]
            move(piles, from_pile, to_pile, n)
        else:
            list_of_chars = line.split()
            print(list_of_chars)
            characters = line[line.find("[")+1:line.find("]")]
            print(characters)
            piles[int(line)].append(line[-1])

    for i, pile in enumerate(piles):
        print("{}: {}".format(i, pile))

if __name__ == "__main__":
    main()
