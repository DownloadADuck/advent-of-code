import sys

def main():
    if len(sys.argv) != 2:
           print("Usage: python3 {} <filename>".format(sys.argv[0]))
           sys.exit(1)

    filename = sys.argv[1]
    with open(filename) as f:
           lines = f.readlines()

    # remove newlines
    lines = [line.strip() for line in lines]

    # remove empty lines
    lines = [line for line in lines if line]

    # split lines into stacks
    stacks = []
    for line in lines:
        if line[0] == '[':
            stacks.append(line)
        else:
            stacks[-1] += line

    # split stacks into crates
    crates = []
    for stack in stacks:
        crates.append(stack.split(' '))

    # remove brackets
    crates = [[crate[1:-1] for crate in stack] for stack in crates]

    # remove empty crates
    crates = [[crate for crate in stack if crate] for stack in crates]

    # remove empty stacks
    crates = [stack for stack in crates if stack]

    # remove empty lines
    lines = [line for line in lines if line]

    # remove instructions
    instructions = lines[len(crates) + 1:]
    #print("instructions:", instructions)

    # parse instructions
    for instruction in instructions:
        instruction = instruction.split(' ')
        if instruction[0] == 'move':
            print("instruction: ", instruction)
            print("initial crates: ", crates)
            move(crates, instruction[1], instruction[3], instruction[5])
            print("after crates: ", crates)
        else:
            print("Invalid instructions:", instruction)
            sys.exit(1)

    # print final arrangement
    for stack in crates:
        print(' '.join(stack))

def move(crates, num, from_stack, to_stack):
    num = int(num)
    from_stack = int(from_stack) - 1
    to_stack = int(to_stack) - 1

    if from_stack < 0 or from_stack >= len(crates):
        print("Invalid from_stack:", from_stack)
        sys.exit(1)
    if to_stack < 0 or to_stack >= len(crates):
        print("Invalid to_stack:", to_stack)
        sys.exit(1)
    if num < 0 or num > len(crates[from_stack]):
        print("num: ", num, "crates number: ", len(crates[from_stack]))
        print("Invalid number of crates:", num)
        sys.exit(1)

    crates[to_stack] += crates[from_stack][-num:]
    crates[from_stack] = crates[from_stack][:-num]

if __name__ == "__main__":
    main()






















