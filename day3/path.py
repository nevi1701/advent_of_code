import re 

def convert(path):
    new_path = list()
    path = path.split(",")
    for items in path:
        match = re.match(r"^([a-z]+)([0-9]+)$", items, re.IGNORECASE)
        if match:
            items = match.groups()
            new_path.append(items)
    return new_path

def cal(paths):
    move_history = list()
    init_x = 0
    init_y = 0
    for path in paths:
        if path[0] == "L":
            for x in range(init_x, init_x - int(path[1]) - 1, -1):
                move_history.append([x, init_y])
            init_x = init_x - int(path[1])
        elif path[0] == "R":
            for x in range(init_x, init_x + int(path[1]) + 1, +1):
                move_history.append([x, init_y])
            init_x = init_x + int(path[1])
        elif path[0] == "U":
            for y in range(init_y, init_y + int(path[1]) + 1, +1):
                move_history.append([init_x, y])
            init_y = init_y + int(path[1])
        elif path[0] == "D":
            for y in range(init_y, init_y - int(path[1]) - 1, -1):
                move_history.append([init_x, y])
            init_y = init_y - int(path[1])
    return(move_history)

def compare(path1, path2):
    intersection = list()
    for i in path1:
        for j in path2:
            if i == j and i != [0, 0]:
                intersection.append(i)
    return intersection



def distance(intersections):
    dis = list()
    for intersection in intersections:
        dis.append(intersection[0] + intersection[1])
    return min(dis)
    

    


def main():
    path1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
    path2 = 'U62,R66,U55,R34,D71,R55,D58,R83'
    print(distance(compare(cal(convert(path1)),cal(convert(path2)))))



if __name__ == "__main__":
    main()
