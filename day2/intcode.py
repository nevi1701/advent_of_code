def cal(data, x, y):
    data[1] = x
    data[2] = y
    i = 0
    while i + 4 < len(data):
        if data[i] == 99:
            i+=1
        elif data[i] == 1:
            data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
            i+=4
        elif data[i] == 2:
            data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
            i+=4
    if(data[0]) == 19690720:
        return(x, y)
    else:
        return None

    
def main():
    data = list()
    
    with open("input.txt") as f:
        f = f.read().split(",")
        for _ in f:
            data.append(int(_))
    for x in range(0,100):
        for y in range(0,100):
            subdata = data.copy()
            if cal(subdata, x, y) != None:
                print(x, y)
            


if __name__ == "__main__":
    main()       

    
