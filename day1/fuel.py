def fuel(mass):
    sum = 0
    while mass > 0:
        mass = (mass//3 - 2)
        if mass > 0:
            sum+=mass
    return sum

def main():
    sum = 0
    with open ("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            sum += fuel(int(line.replace("\n", "")))
    print(sum)

if __name__ == "__main__":
    main()